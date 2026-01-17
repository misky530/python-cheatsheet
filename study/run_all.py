def main():
    import importlib
    for mod_name in ["ch01_collections", "ch02_types", "ch03_syntax", "ch05_data"]:
        print("\n" + "#" * 70)
        print(f"RUN: {mod_name}")
        print("#" * 70)
        mod = importlib.import_module(mod_name)
        mod.main()

if __name__ == "__main__":
    main()
