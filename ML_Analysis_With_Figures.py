#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
نمذجة تعلم الآلة مع الرسوم البيانية
Machine Learning Models with Visualizations for Research
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Arabic font support
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# Check if in Colab
try:
    from google.colab import files
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

# Try XGBoost
try:
    from xgboost import XGBClassifier
    XGBOOST_AVAILABLE = True
except ImportError:
    XGBOOST_AVAILABLE = False
    if IN_COLAB:
        print("⚙️  تثبيت XGBoost...")
        import os
        os.system('pip install xgboost -q')
        try:
            from xgboost import XGBClassifier
            XGBOOST_AVAILABLE = True
        except:
            pass


def upload_file_colab():
    """رفع ملف في Colab"""
    if IN_COLAB:
        print("\n📤 ارفع ملف Excel التحليل:")
        uploaded = files.upload()
        if uploaded:
            return list(uploaded.keys())[0]
    return None


def load_data(file_path):
    """تحميل البيانات"""
    print("\n📖 قراءة البيانات...")
    try:
        df = pd.read_excel(file_path, sheet_name='تحليل الجودة')
        print(f"   ✅ تم تحميل {len(df)} صف")
        return df
    except Exception as e:
        print(f"   ❌ خطأ: {e}")
        return None


def prepare_features(df):
    """إعداد الميزات"""
    print("\n🔧 إعداد الميزات...")
    
    features = pd.DataFrame()
    features['Q4_Pass'] = (df['نجح في السؤال 4'] == 'نعم').astype(int)
    features['Q7_Pass'] = (df['نجح في السؤال 7'] == 'نعم').astype(int)
    
    # Handle contradictions
    if 'تناقض (إحباط+سعادة)' in df.columns:
        features['Emotional_Contradiction'] = (df['تناقض (إحباط+سعادة)'] == 'نعم').astype(int)
    else:
        features['Emotional_Contradiction'] = 0
    
    if 'تناقض (وقت+تحكم)' in df.columns:
        features['Time_Contradiction'] = (df['تناقض (وقت+تحكم)'] == 'نعم').astype(int)
    else:
        features['Time_Contradiction'] = 0
    
    features['Std_Dev'] = pd.to_numeric(df['الانحراف المعياري'], errors='coerce').fillna(0)
    features['Low_Variance'] = (df['انحراف منخفض'] == 'نعم').astype(int)
    
    target = (~df['التقييم النهائي'].str.contains('نظيف', na=False)).astype(int)
    
    print(f"   ✅ {len(features.columns)} ميزات")
    print(f"   📊 نظيف: {(target==0).sum()}, مشبوه/مزيف: {(target==1).sum()}")
    
    return features, target


def train_models(X_train, X_test, y_train, y_test):
    """تدريب النماذج"""
    print("\n🤖 تدريب النماذج...")
    results = []
    
    # Random Forest
    print("   [1/4] Random Forest...")
    rf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)
    rf.fit(X_train, y_train)
    rf_pred = rf.predict(X_test)
    results.append({
        'Algorithm': 'Random Forest',
        'Model': rf,
        'Predictions': rf_pred,
        'Accuracy': accuracy_score(y_test, rf_pred),
        'Precision': precision_score(y_test, rf_pred, zero_division=0),
        'Recall': recall_score(y_test, rf_pred, zero_division=0),
        'F1-Score': f1_score(y_test, rf_pred, zero_division=0)
    })
    
    # SVM
    print("   [2/4] SVM...")
    svm = SVC(kernel='rbf', random_state=42)
    svm.fit(X_train, y_train)
    svm_pred = svm.predict(X_test)
    results.append({
        'Algorithm': 'SVM',
        'Model': svm,
        'Predictions': svm_pred,
        'Accuracy': accuracy_score(y_test, svm_pred),
        'Precision': precision_score(y_test, svm_pred, zero_division=0),
        'Recall': recall_score(y_test, svm_pred, zero_division=0),
        'F1-Score': f1_score(y_test, svm_pred, zero_division=0)
    })
    
    # Logistic Regression
    print("   [3/4] Logistic Regression...")
    lr = LogisticRegression(random_state=42, max_iter=1000)
    lr.fit(X_train, y_train)
    lr_pred = lr.predict(X_test)
    results.append({
        'Algorithm': 'Logistic Regression',
        'Model': lr,
        'Predictions': lr_pred,
        'Accuracy': accuracy_score(y_test, lr_pred),
        'Precision': precision_score(y_test, lr_pred, zero_division=0),
        'Recall': recall_score(y_test, lr_pred, zero_division=0),
        'F1-Score': f1_score(y_test, lr_pred, zero_division=0)
    })
    
    # XGBoost
    if XGBOOST_AVAILABLE:
        print("   [4/4] XGBoost...")
        xgb = XGBClassifier(n_estimators=100, random_state=42, max_depth=5, eval_metric='logloss')
        xgb.fit(X_train, y_train)
        xgb_pred = xgb.predict(X_test)
        results.append({
            'Algorithm': 'XGBoost',
            'Model': xgb,
            'Predictions': xgb_pred,
            'Accuracy': accuracy_score(y_test, xgb_pred),
            'Precision': precision_score(y_test, xgb_pred, zero_division=0),
            'Recall': recall_score(y_test, xgb_pred, zero_division=0),
            'F1-Score': f1_score(y_test, xgb_pred, zero_division=0)
        })
    else:
        print("   [4/4] XGBoost - غير متوفر")
    
    return results, y_test


def plot_performance_comparison(results, output_dir='./'):
    """
    الشكل 1: مقارنة أداء الخوارزميات
    """
    print("\n📊 إنشاء الشكل 1: مقارنة الأداء...")
    
    # Prepare data
    algorithms = [r['Algorithm'] for r in results]
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    
    data = {metric: [r[metric] for r in results] for metric in metrics}
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 7))
    
    x = np.arange(len(algorithms))
    width = 0.2
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
    
    for i, metric in enumerate(metrics):
        offset = width * (i - 1.5)
        bars = ax.bar(x + offset, data[metric], width, label=metric, color=colors[i], alpha=0.8)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.3f}',
                   ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    ax.set_xlabel('Algorithm', fontsize=14, fontweight='bold')
    ax.set_ylabel('Score', fontsize=14, fontweight='bold')
    ax.set_title('Figure 1: Performance Comparison of ML Algorithms\nمقارنة أداء خوارزميات التعلم الآلي', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(algorithms, fontsize=11)
    ax.legend(fontsize=11, loc='lower right')
    ax.set_ylim(0, 1.15)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    filename = f'{output_dir}Figure1_Performance_Comparison.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"   ✅ تم حفظ: {filename}")
    plt.close()
    
    return filename


def plot_confusion_matrix(y_test, y_pred, algorithm_name, output_dir='./'):
    """
    الشكل 2: مصفوفة الارتباك
    """
    print(f"\n📊 إنشاء الشكل 2: مصفوفة الارتباك ({algorithm_name})...")
    
    cm = confusion_matrix(y_test, y_pred)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create heatmap
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=True,
                square=True, linewidths=2, linecolor='black',
                annot_kws={'size': 20, 'weight': 'bold'},
                cbar_kws={'label': 'Count'})
    
    ax.set_xlabel('Predicted Label\nالتسمية المتوقعة', fontsize=14, fontweight='bold')
    ax.set_ylabel('True Label\nالتسمية الفعلية', fontsize=14, fontweight='bold')
    ax.set_title(f'Figure 2: Confusion Matrix - {algorithm_name}\nمصفوفة الارتباك', 
                 fontsize=16, fontweight='bold', pad=20)
    
    # Set tick labels
    ax.set_xticklabels(['Clean\nنظيف', 'Suspicious/Fake\nمشبوه/مزيف'], fontsize=12)
    ax.set_yticklabels(['Clean\nنظيف', 'Suspicious/Fake\nمشبوه/مزيف'], fontsize=12, rotation=0)
    
    plt.tight_layout()
    filename = f'{output_dir}Figure2_Confusion_Matrix.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"   ✅ تم حفظ: {filename}")
    plt.close()
    
    return filename


def plot_feature_importance(model, feature_names, output_dir='./'):
    """
    الشكل 3: أهمية الميزات
    """
    print("\n📊 إنشاء الشكل 3: أهمية الميزات...")
    
    # Get feature importance (only for tree-based models)
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
    else:
        print("   ⚠️  النموذج لا يدعم feature importance")
        return None
    
    # Create DataFrame
    df_importance = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    }).sort_values('Importance', ascending=True)
    
    # Arabic feature names
    feature_names_ar = {
        'Q4_Pass': 'Q4 Attention Check\nسؤال التحقق 4',
        'Q7_Pass': 'Q7 Attention Check\nسؤال التحقق 7',
        'Emotional_Contradiction': 'Emotional Contradiction\nالتناقض العاطفي',
        'Time_Contradiction': 'Time Contradiction\nتناقض الوقت',
        'Std_Dev': 'Standard Deviation\nالانحراف المعياري',
        'Low_Variance': 'Low Variance\nالتباين المنخفض'
    }
    
    df_importance['Feature_AR'] = df_importance['Feature'].map(feature_names_ar)
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 8))
    
    colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(df_importance)))
    bars = ax.barh(df_importance['Feature_AR'], df_importance['Importance'], color=colors, alpha=0.8)
    
    # Add value labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2,
               f'{width:.3f}',
               ha='left', va='center', fontsize=11, fontweight='bold')
    
    ax.set_xlabel('Importance Score', fontsize=14, fontweight='bold')
    ax.set_ylabel('Features', fontsize=14, fontweight='bold')
    ax.set_title('Figure 3: Feature Importance\nأهمية الميزات في التصنيف', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    filename = f'{output_dir}Figure3_Feature_Importance.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"   ✅ تم حفظ: {filename}")
    plt.close()
    
    return filename


def plot_metrics_radar(results, output_dir='./'):
    """
    الشكل 4: مخطط راداري للمقاييس
    """
    print("\n📊 إنشاء الشكل 4: المخطط الراداري...")
    
    # Prepare data
    algorithms = [r['Algorithm'] for r in results]
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    
    # Number of variables
    num_vars = len(metrics)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
    
    for i, result in enumerate(results):
        values = [result[m] for m in metrics]
        values += values[:1]
        
        ax.plot(angles, values, 'o-', linewidth=2, label=result['Algorithm'], 
               color=colors[i % len(colors)], markersize=8)
        ax.fill(angles, values, alpha=0.15, color=colors[i % len(colors)])
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(metrics, fontsize=12, fontweight='bold')
    ax.set_ylim(0, 1.1)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.5)
    
    ax.set_title('Figure 4: Radar Chart of Performance Metrics\nالمخطط الراداري لمقاييس الأداء', 
                 fontsize=16, fontweight='bold', pad=30, y=1.08)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=11)
    
    plt.tight_layout()
    filename = f'{output_dir}Figure4_Radar_Chart.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"   ✅ تم حفظ: {filename}")
    plt.close()
    
    return filename


def plot_roc_curves(models, X_test, y_test, output_dir='./'):
    """
    الشكل 5: منحنيات ROC
    """
    print("\n📊 إنشاء الشكل 5: منحنيات ROC...")
    
    from sklearn.metrics import roc_curve, auc
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
    
    for i, result in enumerate(models):
        if result['Model'] is None:
            continue
            
        # Get probability predictions
        if hasattr(result['Model'], 'predict_proba'):
            y_proba = result['Model'].predict_proba(X_test)[:, 1]
        elif hasattr(result['Model'], 'decision_function'):
            y_proba = result['Model'].decision_function(X_test)
        else:
            continue
        
        fpr, tpr, _ = roc_curve(y_test, y_proba)
        roc_auc = auc(fpr, tpr)
        
        ax.plot(fpr, tpr, linewidth=2.5, label=f"{result['Algorithm']} (AUC = {roc_auc:.3f})",
               color=colors[i % len(colors)])
    
    # Diagonal line
    ax.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Random Classifier', alpha=0.5)
    
    ax.set_xlabel('False Positive Rate (FPR)', fontsize=14, fontweight='bold')
    ax.set_ylabel('True Positive Rate (TPR)', fontsize=14, fontweight='bold')
    ax.set_title('Figure 5: ROC Curves\nمنحنيات خاصية التشغيل للمستقبل', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.legend(loc='lower right', fontsize=11)
    ax.grid(alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    filename = f'{output_dir}Figure5_ROC_Curves.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"   ✅ تم حفظ: {filename}")
    plt.close()
    
    return filename


def create_results_summary(results, best_model, cm, output_file='ML_Results_Summary.xlsx'):
    """
    إنشاء ملف Excel بالنتائج
    """
    print(f"\n💾 إنشاء ملف النتائج: {output_file}...")
    
    # Table 4: Performance Metrics
    df_results = pd.DataFrame([
        {
            'الخوارزمية (Algorithm)': r['Algorithm'],
            'الدقة (Accuracy)': f"{r['Accuracy']:.3f}",
            'الحساسية (Recall)': f"{r['Recall']:.3f}",
            'الدقة (Precision)': f"{r['Precision']:.3f}",
            'F1-Score': f"{r['F1-Score']:.3f}"
        }
        for r in results if r.get('Model') is not None
    ])
    
    # Table 5: Confusion Matrix
    df_cm = pd.DataFrame(
        cm,
        index=['فعلي - نظيف (Actual Clean)', 'فعلي - مزيف (Actual Fake)'],
        columns=['توقع - نظيف (Predicted Clean)', 'توقع - مزيف (Predicted Fake)']
    )
    
    # Summary
    tn, fp, fn, tp = cm.ravel()
    df_summary = pd.DataFrame([
        {'المؤشر': 'Best Algorithm', 'القيمة': best_model['Algorithm']},
        {'المؤشر': 'Best F1-Score', 'القيمة': f"{best_model['F1-Score']:.3f}"},
        {'المؤشر': 'True Negatives', 'القيمة': int(tn)},
        {'المؤشر': 'False Positives', 'القيمة': int(fp)},
        {'المؤشر': 'False Negatives', 'القيمة': int(fn)},
        {'المؤشر': 'True Positives', 'القيمة': int(tp)}
    ])
    
    # Save to Excel
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        df_results.to_excel(writer, sheet_name='Table 4 - Performance', index=False)
        df_cm.to_excel(writer, sheet_name='Table 5 - Confusion Matrix')
        df_summary.to_excel(writer, sheet_name='Summary', index=False)
    
    print(f"   ✅ تم حفظ الملف")
    
    if IN_COLAB:
        files.download(output_file)
    
    return output_file


def main():
    print("\n" + "="*80)
    print("🤖 نمذجة تعلم الآلة مع الرسوم البيانية")
    print("   Machine Learning with Research Visualizations")
    print("="*80)
    
    # Get file
    if IN_COLAB:
        file_path = upload_file_colab()
        if not file_path:
            return
    else:
        try:
            import tkinter as tk
            from tkinter import filedialog
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename(
                title="اختر ملف التحليل",
                filetypes=[("Excel files", "*.xlsx *.xls")]
            )
            root.destroy()
            if not file_path:
                return
        except:
            print("\n❌ لا يمكن فتح نافذة اختيار الملفات")
            return
    
    # Load data
    df = load_data(file_path)
    if df is None:
        return
    
    # Prepare features
    X, y = prepare_features(df)
    
    # Split and scale
    print("\n📊 تقسيم البيانات (70% تدريب، 30% اختبار)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train models
    results, y_test_actual = train_models(X_train_scaled, X_test_scaled, y_train, y_test)
    
    # Find best model
    valid_results = [r for r in results if r.get('Model') is not None]
    best_model = max(valid_results, key=lambda x: x['F1-Score'])
    cm = confusion_matrix(y_test_actual, best_model['Predictions'])
    
    print("\n" + "="*80)
    print("📊 إنشاء الرسوم البيانية...")
    print("="*80)
    
    # Create all figures
    output_dir = './' if not IN_COLAB else './'
    
    figures = []
    
    # Figure 1: Performance Comparison
    fig1 = plot_performance_comparison(valid_results, output_dir)
    figures.append(fig1)
    
    # Figure 2: Confusion Matrix
    fig2 = plot_confusion_matrix(y_test_actual, best_model['Predictions'], 
                                  best_model['Algorithm'], output_dir)
    figures.append(fig2)
    
    # Figure 3: Feature Importance
    fig3 = plot_feature_importance(best_model['Model'], X.columns, output_dir)
    if fig3:
        figures.append(fig3)
    
    # Figure 4: Radar Chart
    fig4 = plot_metrics_radar(valid_results, output_dir)
    figures.append(fig4)
    
    # Figure 5: ROC Curves
    fig5 = plot_roc_curves(valid_results, X_test_scaled, y_test_actual, output_dir)
    figures.append(fig5)
    
    # Create Excel summary
    excel_file = create_results_summary(valid_results, best_model, cm)
    
    print("\n" + "="*80)
    print("✅ اكتمل التحليل!")
    print("="*80)
    
    print("\n📊 الملفات المُنشأة:")
    for i, fig in enumerate(figures, 1):
        if fig:
            print(f"   {i}. {fig}")
    print(f"   6. {excel_file}")
    
    if IN_COLAB:
        print("\n📥 جاري تحميل الصور...")
        for fig in figures:
            if fig:
                try:
                    files.download(fig)
                except:
                    pass
    
    print("\n💡 استخدم هذه الأشكال مباشرة في بحثك!")
    print("   • جودة عالية (300 DPI)")
    print("   • مناسبة للطباعة")
    print("   • بعناوين عربية وإنجليزية")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ خطأ: {e}")
        import traceback
        traceback.print_exc()
        
        if not IN_COLAB:
            input("\nاضغط Enter للخروج...")
