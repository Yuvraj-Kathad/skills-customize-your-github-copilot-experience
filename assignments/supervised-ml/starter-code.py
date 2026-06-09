import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
import joblib


def load_data(path="data.csv"):
    return pd.read_csv(path)


def preprocess(df):
    # Simple example: drop rows with missing label, fill numeric NaNs with median
    df = df.copy()
    df = df.dropna(subset=["label"])
    for c in df.select_dtypes(include=["number"]).columns:
        df[c] = df[c].fillna(df[c].median())
    X = df.drop(columns=["label"]) 
    y = df["label"]
    return X, y


def train_models(X_train, y_train):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train_scaled, y_train)

    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    return scaler, lr, rf


def evaluate_model(model, scaler, X_test, y_test):
    if scaler is not None:
        X = scaler.transform(X_test)
    else:
        X = X_test
    preds = model.predict(X)
    probs = model.predict_proba(X)[:, 1] if hasattr(model, "predict_proba") else None
    metrics = {
        "accuracy": accuracy_score(y_test, preds),
        "precision": precision_score(y_test, preds),
        "recall": recall_score(y_test, preds),
        "f1": f1_score(y_test, preds),
        "roc_auc": roc_auc_score(y_test, probs) if probs is not None else None,
        "confusion_matrix": confusion_matrix(y_test, preds).tolist(),
    }
    return metrics


def save_model(obj, path="model.joblib"):
    joblib.dump(obj, path)


def main():
    df = load_data("data.csv")
    print("Loaded data:", df.shape)
    X = df.drop(columns=["label"])
    y = df["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler, lr, rf = train_models(X_train, y_train)

    print("Evaluating Logistic Regression")
    lr_metrics = evaluate_model(lr, scaler, X_test, y_test)
    print(lr_metrics)

    print("Evaluating Random Forest")
    rf_metrics = evaluate_model(rf, None, X_test, y_test)
    print(rf_metrics)

    # Save the best model stub (choose by accuracy here)
    best = lr if lr_metrics["accuracy"] >= rf_metrics["accuracy"] else rf
    save_model({"scaler": scaler, "model": best}, "model.joblib")
    print("Saved model.joblib")


if __name__ == "__main__":
    main()
