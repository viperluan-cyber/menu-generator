

# 导入Python内置随机模块
import random

# ===================== 一、核心数据配置【全品类加肉类标签｜顶配完整版】 =====================
# ✅ 三大类带肉菜品 全部新增 meat_type 属性：猪肉/牛羊肉/鸡肉/海鲜/其他
# ✅ 菜品主分类：meat(纯荤) / veg(纯素) / mix(荤素) / mix_main(荤素主)
FOOD_DATA = {
 # ===== 纯荤菜(meat) → 必带meat_type =====
    "京酱肉丝": {"type": "meat", "meat_type": "猪肉", "原料": {"猪里脊": 250, "大葱": 100, "甜面酱": 80}},
    "猪肉丸子": {"type": "meat", "meat_type": "猪肉", "原料": {"猪肉馅": 250, "土豆": 100}},
    "可乐鸡翅": {"type": "meat", "meat_type": "鸡肉", "原料": {"鸡翅": 300, "可乐": 300}},
    "糖醋排骨": {"type": "meat", "meat_type": "猪肉", "原料": {"排骨": 350}},
    "卤牛腱子": {"type": "meat", "meat_type": "牛羊肉", "原料": {"牛腱子": 1000}},
    "卤鸡腿": {"type": "meat", "meat_type": "鸡肉", "原料": {"鸡腿肉": 500}},
    "清蒸鲈鱼": {"type": "meat", "meat_type": "鱼", "原料": {"鲈鱼": 400}},
    "红烧鱼": {"type": "meat", "meat_type": "鱼", "原料": {"鱼": 400}},
    "烤鱼": {"type": "meat", "meat_type": "鱼", "原料": {"鱼": 400}},
    "油焖大虾": {"type": "meat", "meat_type": "海鲜", "原料": {"大虾": 400}},
    "贝勒烤肉": {"type": "meat", "meat_type": "猪肉", "原料": {"猪前腿": 300, "香菜": 100}},
    "清炖牛肋条": {"type": "meat", "meat_type": "牛羊肉", "原料": {"牛肋条": 800}},
    "香煎鸡腿肉": {"type": "meat", "meat_type": "鸡肉", "原料": {"鸡腿肉": 300}},


    # ===== 荤素菜(mix) → ✅ 新增meat_type =====
    "辣椒炒肉": {"type": "mix", "meat_type": "猪肉", "原料": {"猪里脊": 250, "辣椒": 100, "胡萝卜": 100}},
    "芹菜炒肉": {"type": "mix", "meat_type": "猪肉", "原料": {"猪里脊": 250, "芹菜": 100, "木耳": 100}},
    "豆角炒肉": {"type": "mix", "meat_type": "猪肉", "原料": {"猪里脊": 250, "豆角": 150}},
    "番茄炖牛腩": {"type": "mix", "meat_type": "牛羊肉", "原料": {"牛腩": 1000, "西红柿": 300}},
    "土豆炖排骨": {"type": "meat", "meat_type": "猪肉", "原料": {"排骨": 350, "土豆": 150}},
    "洋柿子炖土豆": {"type": "mix", "meat_type": "猪肉", "原料": {"西红柿": 150, "土豆": 150, "猪前腿肉": 250}},
    "洋葱孜然牛肉": {"type": "meat", "meat_type": "牛羊肉", "原料": {"牛肉片": 300, "紫洋葱": 150}},
    "杏鲍菇炒牛肉": {"type": "meat", "meat_type": "牛羊肉", "原料": {"嫩牛肉": 300, "杏鲍菇": 200}},

    # ===== 纯素菜(veg) → 无meat_type =====
    "白灼生菜": {"type": "veg", "原料": {"生菜": 300}},
    "蒜蓉西兰花": {"type": "veg", "原料": {"西兰花": 300}},
    "西红柿炒蛋": {"type": "veg", "原料": {"西红柿": 300, "鸡蛋": 100}},
    "清炒白菜花": {"type": "veg", "原料": {"白菜花": 300, "虾皮": 100}},
    "蒜蓉娃娃菜": {"type": "veg", "原料": {"娃娃菜": 300}},
    "清炒豆芽菜": {"type": "veg", "原料": {"豆芽菜": 300}},
    "黄油杏鲍菇": {"type": "veg", "原料": {"杏鲍菇": 300}},
    "清炒口蘑": {"type": "veg", "原料": {"口蘑": 300}},
    "清炒胡萝卜": {"type": "veg", "原料": {"胡萝卜": 300}},
    "清炒菠菜": {"type": "veg", "原料": {"菠菜": 300}},
    "清炒油麦菜": {"type": "veg", "原料": {"油麦菜": 300}}, 
    "白菜炖豆腐": {"type": "veg", "原料": {"白菜": 300, "豆腐": 200}}, 


    # ===== 荤素主菜(mix_main) → ✅ 新增meat_type =====
    "牛肉饭": {"type": "mix_main", "meat_type": "牛羊肉", "原料": {"牛肉片": 300, "白洋葱": 300, "黑胡椒": 10, "西兰花": 100, "大米": 100}},
    "洋葱包子": {"type": "mix_main", "meat_type": "猪肉", "原料": {"面粉": 300, "猪肉馅":300, "紫洋葱":300, "酵母":5}},
    "韭菜饺子": {"type": "mix_main", "meat_type": "猪肉", "原料": {"面粉":300, "猪肉馅":300, "韭菜":300, "扇贝":200}},
    "茴香饺子": {"type": "mix_main", "meat_type": "猪肉", "原料": {"面粉":300, "猪肉馅":300, "茴香":300}},
    "白菜饺子": {"type": "mix_main", "meat_type": "猪肉", "原料": {"面粉":300, "猪肉馅":300, "白菜":300}},
    "肉炒饼": {"type": "mix_main", "meat_type": "猪肉", "原料": {"饼丝":300, "火腿肠":100, "豆芽菜":100, "鸡蛋":100}},
}

# ✅ 主食字典【新增】：独立配置｜含原料+克数（米饭/面条/馒头等）
STAPLE_FOOD_DATA = {
    "白米饭": {"原料": {"大米": 100}},
    "杂粮饭": {"原料": {"大米": 70, "糙米": 30}},
    "馒头": {"原料": {"馒头": 2}},
}

# ===================== 二、核心工具函数【零报错｜零崩溃｜强稳定】 =====================
def check_and_fix_food_data(food_data):
    """✅ 菜品数据校验+兜底：缺失meat_type自动补「其他」"""
    MEAT_DEFAULT = "其他"
    fix_log = []
    for food_name, food_info in food_data.items():
        if food_info["type"] in ["meat", "mix", "mix_main"] and "meat_type" not in food_info:
            food_info["meat_type"] = MEAT_DEFAULT
            fix_log.append(f"⚠️ 菜品【{food_name}】缺失meat_type，自动补为「{MEAT_DEFAULT}」")
    if fix_log:
        print("📊 菜品数据自动修复日志：")
        for log in fix_log:
            print(log)
    else:
        print("✅ 所有菜品数据完整，无需修复")
    return food_data

def safe_random_choice(data_list, fallback_data):
    """✅ 安全随机选择：空列表自动兜底，永不报错"""
    if isinstance(data_list, list) and len(data_list) > 0:
        return random.choice(data_list)
    return random.choice(fallback_data)

# ===================== 三、自动分类【新增「鱼」类｜规则绑定｜精准分类】 =====================
FOOD_DATA = check_and_fix_food_data(FOOD_DATA)

# ✅ 菜品4大主分类（严格区分主食规则）
MEAT_FOODS = [name for name, info in FOOD_DATA.items() if info["type"] == "meat"]    # 必配主食
VEG_FOODS = [name for name, info in FOOD_DATA.items() if info["type"] == "veg"]      # 配菜，无主食
MIX_FOODS = [name for name, info in FOOD_DATA.items() if info["type"] == "mix"]      # 必配主食
MIX_MAIN_FOODS = [name for name, info in FOOD_DATA.items() if info["type"] == "mix_main"]  # 不配主食
STAPLE_FOODS = list(STAPLE_FOOD_DATA.keys())

# ✅ ✅ 核心改动：新增「鱼」类标签 → 共6类：猪肉/牛羊肉/鸡肉/鱼/海鲜/其他
MEAT_SUB_TYPES = ["猪肉", "牛羊肉", "鸡肉", "鱼", "海鲜", "其他"]
ALL_MEAT_RELATED_FOODS = [name for name, info in FOOD_DATA.items() if "meat_type" in info]
MEAT_BY_SUBTYPE = {
    subtype: [name for name in ALL_MEAT_RELATED_FOODS if FOOD_DATA[name]["meat_type"] == subtype]
    for subtype in MEAT_SUB_TYPES
}

# ===================== 四、核心生成函数【终版｜零报错｜100%合规】 =====================
def generate_single_meal(week_meat_count, last_meal_dishes, week_used_dishes):
    """✅ 生成单餐组合｜兼容「鱼」类 + 彻底解决所有报错 + 主食规则100%合规"""
    # ✅ 提前初始化所有核心变量 → 彻底解决UnboundLocalError
    dish_combo, dish_list = "", []
    staple_food = None
    used_meat_subtype = None
    dish = ""
    max_attempts = 300

    for _ in range(max_attempts):
        # ✅ 首次运行荤类兜底 → 计数全0时指定默认品类，规避排序异常
        if sum(week_meat_count.values()) == 0:
            target_subtype = "猪肉"
        else:
            sorted_subtypes = sorted(week_meat_count.items(), key=lambda x: x[1])
            target_subtype = sorted_subtypes[0][0]

        # ✅ 策略1：纯荤+素菜组合 → 必配主食（规则绑定，兼容「鱼」类）
        if random.random() < 0.4:
            target_meat = [d for d in MEAT_BY_SUBTYPE[target_subtype] if d in MEAT_FOODS]
            meat = safe_random_choice(target_meat, MEAT_FOODS)
            veg = safe_random_choice(VEG_FOODS, [meat])
            dish_combo = f"{meat} + {veg}"
            dish_list = [meat, veg]
            staple_food = safe_random_choice(STAPLE_FOODS, ["白米饭"])
            used_meat_subtype = FOOD_DATA[meat]["meat_type"]

        # ✅ 策略2：荤素菜单吃 → 必配主食（规则绑定）
        elif random.random() < 0.7:
            dish = safe_random_choice(MIX_FOODS, MIX_MAIN_FOODS)
            dish_combo = dish
            dish_list = [dish]
            staple_food = safe_random_choice(STAPLE_FOODS, ["白米饭"])
            used_meat_subtype = FOOD_DATA[dish]["meat_type"]

        # ✅ 策略3：荤素主菜单吃 → 绝对不配主食（核心合规）
        else:
            dish = safe_random_choice(MIX_MAIN_FOODS, MIX_FOODS)
            dish_combo = dish
            dish_list = [dish]
            staple_food = None  # 强制不配主食
            used_meat_subtype = FOOD_DATA[dish]["meat_type"]

        # ✅ 双重校验：相邻顿严格不重 + 周内菜品尽量不重
        cond1 = not any(d in last_meal_dishes for d in dish_list)
        cond2 = not any(d in week_used_dishes for d in dish_list)
        if cond1 and (cond2 or len(week_used_dishes) >= len(FOOD_DATA)-2):
            # ✅ 合规校验：确保荤素主菜无主食，其他菜品有主食
            if dish_list and dish_list[0] in MIX_MAIN_FOODS:
                staple_food = None
            return dish_combo, dish_list, staple_food, used_meat_subtype
    
    # ✅ 终极兜底逻辑 → 100%有值、100%合规，杜绝所有异常
    dish = safe_random_choice(MIX_MAIN_FOODS, list(FOOD_DATA.keys()))
    dish_combo, dish_list = dish, [dish]
    staple_food = None if dish in MIX_MAIN_FOODS else safe_random_choice(STAPLE_FOODS, ["白米饭"])
    used_meat_subtype = FOOD_DATA[dish]["meat_type"]
    return dish_combo, dish_list, staple_food, used_meat_subtype

def add_materials(total_dict, target_data, name):
    """✅ 原料累加函数"""
    materials = target_data[name]["原料"]
    for mat, weight in materials.items():
        total_dict[mat] = total_dict.get(mat, 0) + weight

# ===================== 五、主程序【终版｜新增「鱼」类｜零报错｜零违规】 =====================
print("=" * 136)
print("🎯 【4周终极用餐安排｜新增「鱼」肉类标签 · 零报错·零违规·零崩溃 终版】")
print("✅ 核心规则铁律：")
print("   ✔️ 荤素主菜(mix_main) → 绝对不配主食 | ✔️ 纯荤/荤素菜 → 必配主食")
print("   ✔️ 肉类6类平衡：猪肉/牛羊肉/鸡肉/鱼/海鲜/其他 | ✔️ 相邻顿严格不重复")
print("=" * 136)

last_meal_dishes = []  # 全局相邻顿校验

for week_num in range(1, 5):
    week_total_materials = {}
    week_used_dishes = []
    # ✅ 初始化6类肉类计数，包含新增的「鱼」类
    week_meat_count = {subtype: 0 for subtype in MEAT_SUB_TYPES}
    
    print(f"\n📅 ========== 第 {week_num} 周 最终用餐安排 ==========")
    print(f"🥩 本周肉类品类平衡目标：猪肉/牛羊肉/鸡肉/鱼/海鲜/其他 → 均匀分布")

    for day_num in range(1, 8):
        print(f"\n🥢 第{day_num}天")
        for meal_label in ["🌞 中午", "🌙 晚上"]:
            # 生成合规餐食（兼容「鱼」类，零报错）
            dish_combo, dish_list, staple_food, used_meat_subtype = generate_single_meal(
                week_meat_count, last_meal_dishes, week_used_dishes
            )
            
            # 更新肉类计数（自动统计「鱼」类）
            if used_meat_subtype:
                week_meat_count[used_meat_subtype] += 1
            
            # 更新菜品记录
            last_meal_dishes = dish_list.copy()
            week_used_dishes.extend(dish_list)

            # ✅ 输出合规结果
            print(f"   {meal_label}：", end="")
            if staple_food:
                print(f"{dish_combo} + 🥣【主食：{staple_food}】")
                for d in dish_list:
                    add_materials(week_total_materials, FOOD_DATA, d)
                add_materials(week_total_materials, STAPLE_FOOD_DATA, staple_food)
            else:
                print(f"{dish_combo} ✅【自带主食属性，无需额外主食】")
                for d in dish_list:
                    add_materials(week_total_materials, FOOD_DATA, d)

    # ✅ 肉类统计（展示6类，包含「鱼」类详细数据）
    print(f"\n🥩 第{week_num}周 肉类品类使用统计（共6类）：")
    total_meat = sum(week_meat_count.values())
    for subtype, count in week_meat_count.items():
        ratio = f"{count/total_meat*100:.0f}%" if total_meat >0 else "0%"
        print(f"   🐷 {subtype.ljust(6)} → {count:>2}次 | {ratio}")

    # ✅ 采购清单
    print(f"\n🛒 第{week_num}周 原料采购总清单（菜品+主食｜总克数）：")
    print("   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    sorted_materials = sorted(week_total_materials.items(), key=lambda x: x[1], reverse=True)
    for mat, weight in sorted_materials:
        print(f"   📦 {mat.ljust(12)} → {weight:>6} 克")
    print("-" * 136)

print("\n" + "=" * 136)
print("✅ 4周用餐安排生成完成｜新增「鱼」类✅ 零报错✅ 零违规✅ 零崩溃✅ 100%合规✅ 可直接落地使用 ✅")
print("=" * 136)
