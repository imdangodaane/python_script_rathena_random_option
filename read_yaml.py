import yaml

def main():
  with open('option_names.yml', 'r') as f:
    lines = yaml.safe_load(f)
    print('[')
    for i, value in enumerate(lines['Body']):
      # print(i, value)
      print("  '" + value['Option'] + "',")
    print(']')

if __name__ == "__main__":
  main()
