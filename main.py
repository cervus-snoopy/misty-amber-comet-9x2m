import os

LINE = "Your two-factor code is 482916. It dies with me \u2014 along with your bank, your email, and every password you never wrote down. Goodbye."

def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE
    assert 1 <= len(written) <= 199

if __name__ == "__main__":
    main()
