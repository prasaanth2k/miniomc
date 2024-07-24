import subprocess
import json


class Miniomc:
    @staticmethod
    def create_alias(aliasname: str, url: str, username: str, password: str):
        miniocommand = f"mc alias set {aliasname} {url} {username} {password}"
        result = subprocess.run(
            miniocommand, shell=True, capture_output=True, text=True
        )
        if result.returncode == 0:
            return json.dumps({"message": f"{aliasname} added successfully", "code": 0})
        else:
            return json.dumps({"message": f"{result.stderr}", "code": 1})
    @staticmethod
    def remove_alias(aliasname: str):
        miniocommand = f"mc alias remove {aliasname}"
        result = subprocess.run(
            miniocommand, shell=True, capture_output=True, text=True
        )
        if result.returncode == 0:
            return json.dumps(
                {"message": f"{aliasname} removed successfully", "code": 0}
            )
        else:
            return json.dumps({"message": f"{result.stderr}", "code": 1})
    @staticmethod
    def list_all_alias():
        miniocommand = "mc alias list"
        result = subprocess.run(miniocommand, capture_output=True, shell=True, text=True, check=True)
        output = result.stdout
        aliases = []
        lines = output.strip().split('\n')
        for i in range(0, len(lines), 6):
            alias_info = lines[i:i+6]
            alias = {
                "alias": alias_info[0].strip(),
                "URL": alias_info[1].split(':', 1)[1].strip(),
                "AccessKey": alias_info[2].split(':', 1)[1].strip(),
                "SecretKey": alias_info[3].split(':', 1)[1].strip(),
                "API": alias_info[4].split(':', 1)[1].strip(),
                "Path": alias_info[5].split(':', 1)[1].strip()
            }
            aliases.append(alias)
        json_output = json.dumps(aliases, indent=2)
        print(json_output)