def save_results(results):
    import os
    os.makedirs("data", exist_ok=True)

    print(f"[DEBUG] 正在保存 {len(results)} 个页面结果到 TXT")

    with open("data/advogados_raw.txt", "w", encoding="utf-8") as f:
        for block in results:
            f.write(block + "\n" + "=" * 80 + "\n")
    print("\n✅ 所有数据已保存至 data/advogados_raw.txt")