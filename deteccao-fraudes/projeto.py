import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image, display

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_curve,
    roc_auc_score,
    precision_recall_curve,
    average_precision_score,
    precision_score,
    recall_score,
    f1_score
)

# %%
# ============================================================
# 1. CARREGAMENTO DO DATASET
# ============================================================

url = "https://raw.githubusercontent.com/nsethi31/Kaggle-Data-Credit-Card-Fraud-Detection/master/creditcard.csv"

print("Carregando dataset...")

df = pd.read_csv(url)

print("Dataset carregado:", df.shape)


# ============================================================
# 2. PREPARAÇÃO
# ============================================================

df["log_amount"] = np.log1p(df["Amount"])

X = df.drop("Class", axis=1)
y = df["Class"]


# ============================================================
# 3. DIVISÃO TREINO / TESTE
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Treino original:", X_train.shape)
print("Teste:", X_test.shape)


# ============================================================
# 4. AMOSTRA PARA TREINAMENTO
# ============================================================

X_train_amostra, _, y_train_amostra, _ = train_test_split(
    X_train,
    y_train,
    train_size=50000,
    random_state=42,
    stratify=y_train
)

print("Amostra utilizada no treinamento:", X_train_amostra.shape)


# ============================================================
# 5. PADRONIZAÇÃO
# ============================================================

print("Padronizando dados...")

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train_amostra)
X_test_scaled = scaler.transform(X_test)

print("Padronização concluída.")


# ============================================================
# 6. TREINAMENTO
# ============================================================

print("Treinando Regressão Logística...")

modelo_lr = LogisticRegression(
    class_weight="balanced",
    max_iter=300,
    random_state=42
)

modelo_lr.fit(X_train_scaled, y_train_amostra)

print("Treinamento concluído!")


# ============================================================
# 7. PREDIÇÕES
# ============================================================

print("Calculando probabilidades...")

y_pred_lr = modelo_lr.predict(X_test_scaled)

y_proba_lr = modelo_lr.predict_proba(
    X_test_scaled
)[:, 1]

print("Probabilidades calculadas!")


# ============================================================
# 8. RELATÓRIO DE CLASSIFICAÇÃO
# ============================================================

print("\n" + "=" * 60)
print("RELATÓRIO DE CLASSIFICAÇÃO")
print("=" * 60)

print(
    classification_report(
        y_test,
        y_pred_lr
    )
)


# ============================================================
# 9. MATRIZ DE CONFUSÃO
# ============================================================

cm = confusion_matrix(
    y_test,
    y_pred_lr
)

print("\nMatriz de Confusão:")
print(cm)

tn, fp, fn, tp = cm.ravel()

print("\nDetalhamento:")
print("Verdadeiros Negativos:", tn)
print("Falsos Positivos:", fp)
print("Falsos Negativos:", fn)
print("Verdadeiros Positivos:", tp)


# ============================================================
# 10. CURVA ROC
# ============================================================

fpr, tpr, thresholds_roc = roc_curve(
    y_test,
    y_proba_lr
)

roc_auc = roc_auc_score(
    y_test,
    y_proba_lr
)

print("\nROC AUC:", roc_auc)

plt.figure(figsize=(8, 6))

plt.plot(
    fpr,
    tpr,
    label=f"Regressão Logística (AUC = {roc_auc:.4f})"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--",
    label="Classificador aleatório"
)

plt.xlabel("Taxa de Falsos Positivos")
plt.ylabel("Taxa de Verdadeiros Positivos")
plt.title("Curva ROC — Regressão Logística")
plt.legend()
plt.grid()

plt.savefig(
    "curva_roc.png",
    dpi=150,
    bbox_inches="tight"
)

display(Image(filename="curva_roc.png"))

plt.close()

print("Gráfico ROC salvo como: curva_roc.png")


# ============================================================
# 11. CURVA PRECISION-RECALL
# ============================================================

precision, recall, thresholds_pr = precision_recall_curve(
    y_test,
    y_proba_lr
)

average_precision = average_precision_score(
    y_test,
    y_proba_lr
)

print("Average Precision:", average_precision)

plt.figure(figsize=(8, 6))

plt.plot(
    recall,
    precision,
    label=f"Regressão Logística (AP = {average_precision:.4f})"
)

plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Curva Precision-Recall — Regressão Logística")
plt.legend()
plt.grid()

plt.savefig(
    "curva_precision_recall.png",
    dpi=150,
    bbox_inches="tight"
)

display(Image(filename="curva_precision_recall.png"))

plt.close()

print("Gráfico Precision-Recall salvo como: curva_precision_recall.png")


# ============================================================
# 12. TESTE DOS LIMIARES
# ============================================================

print("\n" + "=" * 60)
print("ANÁLISE DE DIFERENTES LIMIARES")
print("=" * 60)

thresholds = [
    0.10,
    0.20,
    0.30,
    0.40,
    0.50,
    0.60,
    0.70,
    0.80,
    0.90
]

resultados_threshold = []

for threshold in thresholds:

    y_pred_threshold = (
        y_proba_lr >= threshold
    ).astype(int)

    precision_threshold = precision_score(
        y_test,
        y_pred_threshold,
        zero_division=0
    )

    recall_threshold = recall_score(
        y_test,
        y_pred_threshold,
        zero_division=0
    )

    f1_threshold = f1_score(
        y_test,
        y_pred_threshold,
        zero_division=0
    )

    cm_threshold = confusion_matrix(
        y_test,
        y_pred_threshold
    )

    tn, fp, fn, tp = cm_threshold.ravel()

    resultados_threshold.append({
        "Threshold": threshold,
        "Precision": precision_threshold,
        "Recall": recall_threshold,
        "F1": f1_threshold,
        "Falsos_Positivos": fp,
        "Falsos_Negativos": fn
    })


# ============================================================
# 13. RESULTADOS DOS LIMIARES
# ============================================================

df_threshold = pd.DataFrame(
    resultados_threshold
)

print("\nResultados por limiar:")

print(
    df_threshold.to_string(
        index=False,
        float_format=lambda x: f"{x:.4f}"
    )
)


# ============================================================
# 14. SALVAR RESULTADOS
# ============================================================

df_threshold.to_csv(
    "resultados_threshold.csv",
    index=False
)

print("\nTabela salva como: resultados_threshold.csv")

print("\nExecução concluída!")

# %%
# ============================================================
# 15. RANDOM FOREST
# ============================================================

print("\n" + "=" * 60)
print("RANDOM FOREST")
print("=" * 60)

print("\nTreinando Random Forest...")

modelo_rf = RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

modelo_rf.fit(
    X_train_amostra,
    y_train_amostra
)

print("Treinamento do Random Forest concluído!")


# ============================================================
# 16. PREDIÇÕES DO RANDOM FOREST
# ============================================================

y_pred_rf = modelo_rf.predict(X_test)

y_proba_rf = modelo_rf.predict_proba(X_test)[:, 1]


# ============================================================
# 17. AVALIAÇÃO DO RANDOM FOREST
# ============================================================

print("\nRelatório de classificação — Random Forest:")

print(
    classification_report(
        y_test,
        y_pred_rf
    )
)


# ============================================================
# 18. MATRIZ DE CONFUSÃO
# ============================================================

cm_rf = confusion_matrix(
    y_test,
    y_pred_rf
)

print("\nMatriz de Confusão — Random Forest:")
print(cm_rf)

tn_rf, fp_rf, fn_rf, tp_rf = cm_rf.ravel()

print("\nDetalhamento:")
print("Verdadeiros Negativos:", tn_rf)
print("Falsos Positivos:", fp_rf)
print("Falsos Negativos:", fn_rf)
print("Verdadeiros Positivos:", tp_rf)


# ============================================================
# 19. ROC AUC
# ============================================================

roc_auc_rf = roc_auc_score(
    y_test,
    y_proba_rf
)

print("\nROC AUC — Random Forest:", roc_auc_rf)


# ============================================================
# 20. AVERAGE PRECISION
# ============================================================

average_precision_rf = average_precision_score(
    y_test,
    y_proba_rf
)

print(
    "Average Precision — Random Forest:",
    average_precision_rf
)

# ============================================================
# 21. COMPARAÇÃO DOS MODELOS
# ============================================================

precision_lr = precision_score(y_test, y_pred_lr, zero_division=0)
recall_lr = recall_score(y_test, y_pred_lr, zero_division=0)
f1_lr = f1_score(y_test, y_pred_lr, zero_division=0)

precision_rf = precision_score(y_test, y_pred_rf, zero_division=0)
recall_rf = recall_score(y_test, y_pred_rf, zero_division=0)
f1_rf = f1_score(y_test, y_pred_rf, zero_division=0)

# Recalcula a matriz de confusão da Regressão Logística
cm_lr_comparacao = confusion_matrix(y_test, y_pred_lr)
tn_lr_comparacao, fp_lr_comparacao, fn_lr_comparacao, tp_lr_comparacao = cm_lr_comparacao.ravel()

# Recalcula a matriz de confusão do Random Forest
cm_rf_comparacao = confusion_matrix(y_test, y_pred_rf)
tn_rf_comparacao, fp_rf_comparacao, fn_rf_comparacao, tp_rf_comparacao = cm_rf_comparacao.ravel()

comparacao_modelos = pd.DataFrame({
    "Modelo": [
        "Regressão Logística",
        "Random Forest"
    ],
    "Precision_Fraude": [
        precision_lr,
        precision_rf
    ],
    "Recall_Fraude": [
        recall_lr,
        recall_rf
    ],
    "F1_Fraude": [
        f1_lr,
        f1_rf
    ],
    "ROC_AUC": [
        roc_auc,
        roc_auc_rf
    ],
    "Average_Precision": [
        average_precision,
        average_precision_rf
    ],
    "Falsos_Positivos": [
        fp_lr_comparacao,
        fp_rf_comparacao
    ],
    "Falsos_Negativos": [
        fn_lr_comparacao,
        fn_rf_comparacao
    ]
})

print("\n============================================================")
print("COMPARAÇÃO DOS MODELOS")
print("============================================================")

print(comparacao_modelos.to_string(index=False))

comparacao_modelos.to_csv(
    "comparacao_modelos.csv",
    index=False
)

print("\nTabela salva como: comparacao_modelos.csv")

# ============================================================
# 22. TESTE DOS LIMIARES — RANDOM FOREST
# ============================================================

print("\n" + "=" * 60)
print("ANÁLISE DE DIFERENTES LIMIARES — RANDOM FOREST")
print("=" * 60)

thresholds_rf = [
    0.10,
    0.20,
    0.30,
    0.40,
    0.50,
    0.60,
    0.70,
    0.80,
    0.90
]

resultados_threshold_rf = []

for threshold in thresholds_rf:

    y_pred_threshold_rf = (
        y_proba_rf >= threshold
    ).astype(int)

    precision_threshold_rf = precision_score(
        y_test,
        y_pred_threshold_rf,
        zero_division=0
    )

    recall_threshold_rf = recall_score(
        y_test,
        y_pred_threshold_rf,
        zero_division=0
    )

    f1_threshold_rf = f1_score(
        y_test,
        y_pred_threshold_rf,
        zero_division=0
    )

    cm_threshold_rf = confusion_matrix(
        y_test,
        y_pred_threshold_rf
    )

    tn_rf_threshold, fp_rf_threshold, fn_rf_threshold, tp_rf_threshold = (
        cm_threshold_rf.ravel()
    )

    resultados_threshold_rf.append({
        "Threshold": threshold,
        "Precision": precision_threshold_rf,
        "Recall": recall_threshold_rf,
        "F1": f1_threshold_rf,
        "Falsos_Positivos": fp_rf_threshold,
        "Falsos_Negativos": fn_rf_threshold
    })


# ============================================================
# 23. RESULTADOS DOS LIMIARES — RANDOM FOREST
# ============================================================

df_threshold_rf = pd.DataFrame(
    resultados_threshold_rf
)

print("\nResultados por limiar — Random Forest:")

print(
    df_threshold_rf.to_string(
        index=False,
        float_format=lambda x: f"{x:.4f}"
    )
)


# ============================================================
# 24. SALVAR RESULTADOS — RANDOM FOREST
# ============================================================

df_threshold_rf.to_csv(
    "resultados_threshold_random_forest.csv",
    index=False
)

print(
    "\nTabela salva como: "
    "resultados_threshold_random_forest.csv"
)

# ============================================================
# 25. GRÁFICO PRECISION x RECALL — RANDOM FOREST
# ============================================================

plt.figure(figsize=(8, 6))

plt.plot(
    df_threshold_rf["Threshold"],
    df_threshold_rf["Precision"],
    marker="o",
    label="Precision"
)

plt.plot(
    df_threshold_rf["Threshold"],
    df_threshold_rf["Recall"],
    marker="o",
    label="Recall"
)

plt.xlabel("Limiar")
plt.ylabel("Valor")
plt.title("Precision x Recall por Limiar — Random Forest")
plt.legend()
plt.grid()

plt.savefig(
    "precision_recall_threshold_random_forest.png",
    dpi=150,
    bbox_inches="tight"
)

display(Image(filename="precision_recall_threshold_random_forest.png"))

plt.close()

print(
    "\nGráfico salvo como: "
    "precision_recall_threshold_random_forest.png"
)


# ============================================================
# 26. GRÁFICO FALSOS POSITIVOS x FALSOS NEGATIVOS
# ============================================================

plt.figure(figsize=(8, 6))

plt.plot(
    df_threshold_rf["Threshold"],
    df_threshold_rf["Falsos_Positivos"],
    marker="o",
    label="Falsos Positivos"
)

plt.plot(
    df_threshold_rf["Threshold"],
    df_threshold_rf["Falsos_Negativos"],
    marker="o",
    label="Falsos Negativos"
)

plt.xlabel("Limiar")
plt.ylabel("Quantidade")
plt.title("Falsos Positivos x Falsos Negativos — Random Forest")
plt.legend()
plt.grid()

plt.savefig(
    "erros_threshold_random_forest.png",
    dpi=150,
    bbox_inches="tight"
)

display(Image(filename="erros_threshold_random_forest.png"))

plt.close()

print(
    "Gráfico salvo como: "
    "erros_threshold_random_forest.png"
)

# ============================================================
# 27. IMPORTÂNCIA DAS VARIÁVEIS — RANDOM FOREST
# ============================================================

importancia_rf = pd.DataFrame({
    "Variavel": X_train_amostra.columns,
    "Importancia": modelo_rf.feature_importances_
})

importancia_rf = importancia_rf.sort_values(
    "Importancia",
    ascending=False
)

print("\n" + "=" * 60)
print("IMPORTÂNCIA DAS VARIÁVEIS — RANDOM FOREST")
print("=" * 60)

print(
    importancia_rf.to_string(
        index=False,
        float_format=lambda x: f"{x:.6f}"
    )
)


# ============================================================
# 28. GRÁFICO DAS VARIÁVEIS MAIS IMPORTANTES
# ============================================================

top_n = 15

importancia_top = importancia_rf.head(top_n)

plt.figure(figsize=(10, 7))

plt.barh(
    importancia_top["Variavel"][::-1],
    importancia_top["Importancia"][::-1]
)

plt.xlabel("Importância")
plt.ylabel("Variável")
plt.title(
    "15 Variáveis Mais Importantes — Random Forest"
)

plt.grid(axis="x")

plt.savefig(
    "importancia_variaveis_random_forest.png",
    dpi=150,
    bbox_inches="tight"
)

display(Image(filename="importancia_variaveis_random_forest.png"))

plt.close()

print(
    "\nGráfico salvo como: "
    "importancia_variaveis_random_forest.png"
)


# ============================================================
# 29. SALVAR IMPORTÂNCIA DAS VARIÁVEIS
# ============================================================

importancia_rf.to_csv(
    "importancia_variaveis_random_forest.csv",
    index=False
)

print(
    "Tabela salva como: "
    "importancia_variaveis_random_forest.csv"
)

# ============================================================
# 30. INTERPRETAÇÃO DO RANDOM FOREST COM SHAP
# ============================================================

import shap

print("\n" + "=" * 60)
print("INTERPRETAÇÃO COM SHAP")
print("=" * 60)

print("\nCriando amostra para análise SHAP...")

# Utiliza apenas 1.000 registros do teste
X_shap = X_test.sample(
    n=min(1000, len(X_test)),
    random_state=42
)

print("Amostra utilizada pelo SHAP:", X_shap.shape)

print("\nCalculando valores SHAP...")

explainer = shap.TreeExplainer(modelo_rf)

shap_values = explainer.shap_values(X_shap)

print("Valores SHAP calculados!")


# ============================================================
# 31. GRÁFICO DE IMPORTÂNCIA SHAP
# ============================================================

print("\nGerando gráfico SHAP...")

shap.summary_plot(
    shap_values[:, :, 1],
    X_shap,
    show=False
)

fig = plt.gcf()

fig.savefig(
    "shap_importancia.png",
    dpi=150,
    bbox_inches="tight"
)

display(Image(filename="shap_importancia.png"))

plt.close(fig)

print("Gráfico salvo como: shap_importancia.png")


# %%
# ============================================================
# 32. IMPORTÂNCIA MÉDIA DAS VARIÁVEIS — SHAP
# ============================================================

importancia_shap = pd.DataFrame({
    "Variavel": X_shap.columns,
    "Importancia_SHAP": np.abs(shap_values[:, :, 1]).mean(axis=0)
})

importancia_shap = importancia_shap.sort_values(
    "Importancia_SHAP",
    ascending=False
)

print("\n" + "=" * 60)
print("IMPORTÂNCIA MÉDIA DAS VARIÁVEIS — SHAP")
print("=" * 60)

print(
    importancia_shap.to_string(
        index=False,
        float_format=lambda x: f"{x:.6f}"
    )
)


# ============================================================
# 33. SALVAR IMPORTÂNCIA SHAP
# ============================================================

importancia_shap.to_csv(
    "importancia_shap.csv",
    index=False
)

print(
    "\nTabela salva como: "
    "importancia_shap.csv"
)