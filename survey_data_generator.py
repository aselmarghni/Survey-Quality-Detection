#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مولد بيانات الاستبيان - استخدام وسائل التواصل الاجتماعي
يولد بيانات نظيفة وأنواع مختلفة من البيانات المزيفة لأغراض البحث
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import string

class SurveyDataGenerator:
    """
    مولد بيانات الاستبيان مع أنواع مختلفة من الغش
    """
    
    def __init__(self):
        # البيانات الديموغرافية
        self.genders = ['ذكر', 'أنثى']
        self.age_groups = ['أقل من 20', 'من ٢٠ إلى ٣٠ سنة', 'من ٣١ إلى ٤٠ سنة', 
                          'من ٤١ إلى ٥٠ سنة', 'أكثر من ٥٠ سنة']
        self.education = ['ثانوي فأقل', 'دبلوم', 'بكالوريوس', 'ماجستير', 'دكتوراه']
        self.countries = ['السعودية', 'مصر', 'الإمارات', 'الأردن', 'العراق', 
                         'سوريا', 'لبنان', 'الكويت', 'البحرين', 'عمان']
        self.employment = ['طالب', 'موظف', 'لا أعمل', 'متقاعد', 'أعمال حرة']
        self.hours = ['أقل من 3 ساعات يوميًا', 'من 3 إلى أقل من 5 ساعات', 
                     'من 5 ساعات إلى أقل من 7 ساعات', '7 ساعات فأكثر']
        
        # مقياس ليكرت
        self.likert = ['موافق بشدة', 'موافق', 'محايد', 'غير موافق', 'غير موافق بشدة']
        
        # أسماء الأعمدة
        self.columns = [
            'طابع زمني',
            '1- الجنس',
            '2- العمر',
            '3- المستوى التعليمي',
            '4- الدولة',
            '5- الحالة الوظيفية',
            '6- عدد ساعات استخدام وسائل التواصل الاجتماعي',
            '1- أستخدم وسائل التواصل الاجتماعي بشكل يومي',
            '2- ساعدتني وسائل التواصل الاجتماعي في تطوير مهاراتي المهنية',
            '3- أمارس الرياضة بانتظام بتشجيع من وسائل التواصل الاجتماعي',
            '4- يرجى اختيار "محايد" لهذا السؤال ',
            '5- أفضل التسوق عبر الإنترنت على التسوق التقليدي',
            '6- أشعر بالإحباط بعد استخدام وسائل التواصل الاجتماعي',
            '7- يرجى اختيار "موافق بشدة" لهذا السؤال ',
            '8- أشعر أن وسائل التواصل الاجتماعي تهدر الكثير من وقتي',
            '9- أستطيع التحكم في الوقت الذي أقضيه على وسائل التواصل الاجتماعي',
            '10- أشعر بالسعادة في معظم الأوقات أثناء استخدام وسائل التواصل الاجتماعي',
            '11- تشجعني وسائل التواصل الاجتماعي على قراءة الكتب الإلكترونية اكثر من الورقية',
            '12- أتفاعل بنشر المعلومات الموثقة عبر وسائل التواصل الاجتماعي',
            'اذكر أهم ثلاثة عيوب من وجهة نظرك في استخدام وسائل التواصل الاجتماعي (اكتب كل عيب في سطر منفصل)'
        ]
        
        # قائمة عيوب واقعية
        self.common_negatives = [
            'إهدار الوقت',
            'نشر الإشاعات والأخبار الكاذبة',
            'التأثير السلبي على الصحة النفسية',
            'ضعف التواصل الاجتماعي الحقيقي',
            'الإدمان على وسائل التواصل',
            'انتهاك الخصوصية',
            'التنمر الإلكتروني',
            'المقارنة مع الآخرين',
            'التشتت وقلة التركيز',
            'المحتوى السلبي والمضلل'
        ]
    
    def generate_timestamp(self, base_time, minutes_offset):
        """توليد طابع زمني"""
        new_time = base_time + timedelta(minutes=minutes_offset)
        return new_time.strftime('%Y/%m/%d %-I:%M:%S %p غرينتش+3')
    
    def generate_clean_data(self, n=50):
        """توليد بيانات نظيفة وواقعية"""
        print(f"📊 توليد {n} رد نظيف...")
        data = []
        base_time = datetime.now()
        
        for i in range(n):
            # توليد طابع زمني واقعي
            timestamp = self.generate_timestamp(base_time, i * random.randint(5, 30))
            
            # البيانات الديموغرافية
            gender = random.choice(self.genders)
            age = random.choice(self.age_groups)
            education = random.choice(self.education)
            country = random.choice(self.countries)
            employment = random.choice(self.employment)
            hours = random.choice(self.hours)
            
            # توليد إجابات منطقية ومتسقة
            # معظم الناس يستخدمون يومياً
            q1 = random.choice(['موافق بشدة', 'موافق', 'موافق'])
            
            # التطوير المهني متباين
            q2 = random.choice(self.likert)
            
            # الرياضة - معظم الناس لا يمارسون بسبب وسائل التواصل
            q3 = random.choice(['غير موافق', 'غير موافق بشدة', 'محايد'])
            
            # سؤال التحقق 1 - يجب أن يكون محايد
            q4 = 'محايد'
            
            # التسوق الإلكتروني
            q5 = random.choice(self.likert)
            
            # الإحباط
            q6_val = random.randint(1, 5)
            q6 = self.likert[5 - q6_val]  # عكس الترتيب
            
            # سؤال التحقق 2 - يجب أن يكون موافق بشدة
            q7 = 'موافق بشدة'
            
            # هدر الوقت
            q8_val = random.randint(2, 5)
            q8 = self.likert[5 - q8_val]
            
            # التحكم بالوقت - يجب أن يكون معكوس لهدر الوقت
            q9_val = 6 - q8_val + random.randint(-1, 1)
            q9_val = max(1, min(5, q9_val))
            q9 = self.likert[5 - q9_val]
            
            # السعادة - يجب أن تكون معكوسة للإحباط
            q10_val = 6 - q6_val + random.randint(-1, 1)
            q10_val = max(1, min(5, q10_val))
            q10 = self.likert[5 - q10_val]
            
            # الكتب الإلكترونية
            q11 = random.choice(self.likert)
            
            # نشر المعلومات الموثقة
            q12 = random.choice(self.likert)
            
            # السؤال المفتوح - 3 عيوب عشوائية
            negatives = random.sample(self.common_negatives, 3)
            q13 = '\n'.join([f'{i+1}- {neg}' for i, neg in enumerate(negatives)])
            
            row = [timestamp, gender, age, education, country, employment, hours,
                   q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13]
            
            data.append(row)
        
        return pd.DataFrame(data, columns=self.columns)
    
    def generate_failed_attention_checks(self, n=10):
        """توليد ردود فشلت في أسئلة التحقق"""
        print(f"⚠️ توليد {n} رد فاشل في أسئلة التحقق...")
        data = []
        base_time = datetime.now()
        
        for i in range(n):
            timestamp = self.generate_timestamp(base_time, i * random.randint(5, 20))
            
            gender = random.choice(self.genders)
            age = random.choice(self.age_groups)
            education = random.choice(self.education)
            country = random.choice(self.countries)
            employment = random.choice(self.employment)
            hours = random.choice(self.hours)
            
            q1 = random.choice(self.likert)
            q2 = random.choice(self.likert)
            q3 = random.choice(self.likert)
            
            # فشل في السؤال 4 - اختار غير محايد
            q4 = random.choice(['موافق بشدة', 'موافق', 'غير موافق', 'غير موافق بشدة'])
            
            q5 = random.choice(self.likert)
            q6 = random.choice(self.likert)
            
            # فشل في السؤال 7 - اختار غير موافق بشدة
            if random.random() < 0.5:
                q7 = random.choice(['موافق', 'محايد', 'غير موافق', 'غير موافق بشدة'])
            else:
                q7 = 'موافق بشدة'  # أحياناً ينجح في واحد فقط
            
            q8 = random.choice(self.likert)
            q9 = random.choice(self.likert)
            q10 = random.choice(self.likert)
            q11 = random.choice(self.likert)
            q12 = random.choice(self.likert)
            
            q13 = 'لا أعرف'
            
            row = [timestamp, gender, age, education, country, employment, hours,
                   q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13]
            
            data.append(row)
        
        return pd.DataFrame(data, columns=self.columns)
    
    def generate_contradictory_responses(self, n=10):
        """توليد ردود متناقضة"""
        print(f"🔄 توليد {n} رد متناقض...")
        data = []
        base_time = datetime.now()
        
        for i in range(n):
            timestamp = self.generate_timestamp(base_time, i * random.randint(5, 20))
            
            gender = random.choice(self.genders)
            age = random.choice(self.age_groups)
            education = random.choice(self.education)
            country = random.choice(self.countries)
            employment = random.choice(self.employment)
            hours = random.choice(self.hours)
            
            q1 = random.choice(self.likert)
            q2 = random.choice(self.likert)
            q3 = random.choice(self.likert)
            q4 = 'محايد'
            q5 = random.choice(self.likert)
            
            # تناقض: إحباط عالي + سعادة عالية
            q6 = random.choice(['موافق بشدة', 'موافق'])  # إحباط عالي
            q10 = random.choice(['موافق بشدة', 'موافق'])  # سعادة عالية (متناقض!)
            
            q7 = 'موافق بشدة'
            
            # تناقض: هدر وقت عالي + تحكم عالي
            q8 = random.choice(['موافق بشدة', 'موافق'])  # هدر وقت
            q9 = random.choice(['موافق بشدة', 'موافق'])  # تحكم عالي (متناقض!)
            
            q11 = random.choice(self.likert)
            q12 = random.choice(self.likert)
            
            negatives = random.sample(self.common_negatives, 3)
            q13 = '\n'.join(negatives)
            
            row = [timestamp, gender, age, education, country, employment, hours,
                   q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13]
            
            data.append(row)
        
        return pd.DataFrame(data, columns=self.columns)
    
    def generate_straight_lining(self, n=5):
        """توليد ردود مستقيمة (نفس الإجابة لكل شيء)"""
        print(f"➡️ توليد {n} رد مستقيم...")
        data = []
        base_time = datetime.now()
        
        for i in range(n):
            timestamp = self.generate_timestamp(base_time, i * random.randint(2, 10))
            
            gender = random.choice(self.genders)
            age = random.choice(self.age_groups)
            education = random.choice(self.education)
            country = random.choice(self.countries)
            employment = random.choice(self.employment)
            hours = random.choice(self.hours)
            
            # اختيار إجابة واحدة لكل الأسئلة
            answer = random.choice(['موافق', 'محايد', 'موافق بشدة'])
            
            q1 = answer
            q2 = answer
            q3 = answer
            q4 = answer  # حتى أسئلة التحقق!
            q5 = answer
            q6 = answer
            q7 = answer
            q8 = answer
            q9 = answer
            q10 = answer
            q11 = answer
            q12 = answer
            
            q13 = 'نفس الشيء'
            
            row = [timestamp, gender, age, education, country, employment, hours,
                   q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13]
            
            data.append(row)
        
        return pd.DataFrame(data, columns=self.columns)
    
    def generate_duplicate_responses(self, n=8):
        """توليد ردود مكررة (نفس الشخص يجيب عدة مرات)"""
        print(f"📋 توليد {n} رد مكرر...")
        data = []
        base_time = datetime.now()
        
        # إنشاء 2-3 أنماط وتكرار كل واحد
        num_patterns = 2
        patterns = []
        
        for _ in range(num_patterns):
            pattern = {
                'gender': random.choice(self.genders),
                'age': random.choice(self.age_groups),
                'education': random.choice(self.education),
                'country': random.choice(self.countries),
                'employment': random.choice(self.employment),
                'hours': random.choice(self.hours),
                'answers': [random.choice(self.likert) for _ in range(12)]
            }
            pattern['answers'][3] = 'محايد'  # السؤال 4
            pattern['answers'][6] = 'موافق بشدة'  # السؤال 7
            patterns.append(pattern)
        
        for i in range(n):
            # استخدام نفس النمط
            pattern = patterns[i % num_patterns]
            
            timestamp = self.generate_timestamp(base_time, i * random.randint(2, 5))
            
            q13 = 'نفس العيوب السابقة'
            
            row = [
                timestamp,
                pattern['gender'],
                pattern['age'],
                pattern['education'],
                pattern['country'],
                pattern['employment'],
                pattern['hours']
            ] + pattern['answers'] + [q13]
            
            data.append(row)
        
        return pd.DataFrame(data, columns=self.columns)
    
    def generate_random_nonsense(self, n=7):
        """توليد ردود عشوائية تماماً"""
        print(f"🎲 توليد {n} رد عشوائي...")
        data = []
        base_time = datetime.now()
        
        for i in range(n):
            timestamp = self.generate_timestamp(base_time, i * random.randint(1, 5))
            
            gender = random.choice(self.genders)
            age = random.choice(self.age_groups)
            education = random.choice(self.education)
            country = random.choice(self.countries)
            employment = random.choice(self.employment)
            hours = random.choice(self.hours)
            
            # كل شيء عشوائي تماماً
            q1 = random.choice(self.likert)
            q2 = random.choice(self.likert)
            q3 = random.choice(self.likert)
            q4 = random.choice(self.likert)  # فشل
            q5 = random.choice(self.likert)
            q6 = random.choice(self.likert)
            q7 = random.choice(self.likert)  # فشل
            q8 = random.choice(self.likert)
            q9 = random.choice(self.likert)
            q10 = random.choice(self.likert)
            q11 = random.choice(self.likert)
            q12 = random.choice(self.likert)
            
            # كلام عشوائي
            q13 = ''.join(random.choices(string.ascii_lowercase, k=20))
            
            row = [timestamp, gender, age, education, country, employment, hours,
                   q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13]
            
            data.append(row)
        
        return pd.DataFrame(data, columns=self.columns)
    
    def generate_complete_dataset(self, clean=50, failed_attention=10, 
                                  contradictory=10, straight=5, 
                                  duplicate=8, random_resp=7):
        """توليد مجموعة بيانات كاملة"""
        print("\n" + "=" * 80)
        print("🚀 بدء توليد مجموعة البيانات الكاملة")
        print("=" * 80 + "\n")
        
        # توليد كل نوع
        df_clean = self.generate_clean_data(clean)
        df_failed = self.generate_failed_attention_checks(failed_attention)
        df_contradictory = self.generate_contradictory_responses(contradictory)
        df_straight = self.generate_straight_lining(straight)
        df_duplicate = self.generate_duplicate_responses(duplicate)
        df_random = self.generate_random_nonsense(random_resp)
        
        # دمج كل البيانات
        all_data = pd.concat([
            df_clean,
            df_failed,
            df_contradictory,
            df_straight,
            df_duplicate,
            df_random
        ], ignore_index=True)
        
        # خلط البيانات
        all_data = all_data.sample(frac=1).reset_index(drop=True)
        
        print("\n" + "=" * 80)
        print("✅ تم إنشاء البيانات بنجاح!")
        print("=" * 80)
        print(f"\n📊 إحصائيات:")
        print(f"   - ردود نظيفة: {clean}")
        print(f"   - فشل في أسئلة التحقق: {failed_attention}")
        print(f"   - ردود متناقضة: {contradictory}")
        print(f"   - ردود مستقيمة: {straight}")
        print(f"   - ردود مكررة: {duplicate}")
        print(f"   - ردود عشوائية: {random_resp}")
        print(f"   {'─' * 40}")
        print(f"   - الإجمالي: {len(all_data)} رد")
        
        return all_data


def main():
    """الدالة الرئيسية"""
    print("\n" + "=" * 80)
    print("📋 مولد بيانات الاستبيان - استخدام وسائل التواصل الاجتماعي")
    print("=" * 80)
    
    # إنشاء المولد
    generator = SurveyDataGenerator()
    
    # توليد البيانات
    dataset = generator.generate_complete_dataset(
        clean=50,              # 50 رد نظيف
        failed_attention=10,   # 10 فشلوا في أسئلة التحقق
        contradictory=10,      # 10 ردود متناقضة
        straight=5,            # 5 ردود مستقيمة
        duplicate=8,           # 8 ردود مكررة
        random_resp=7          # 7 ردود عشوائية
    )
    
    # حفظ البيانات
    output_file = 'survey_fake_data.csv'
    dataset.to_csv(output_file, index=False, encoding='utf-8-sig')
    
    print(f"\n💾 تم حفظ البيانات في: {output_file}")
    print("\n" + "=" * 80)
    print("✨ انتهى!")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    # تعيين البذرة للحصول على نتائج قابلة للتكرار
    random.seed(42)
    np.random.seed(42)
    
    main()
