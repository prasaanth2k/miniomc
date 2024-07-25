import subprocess
import json
from typing import Union


class Response:
    def __init__(self, data: dict):
        """
        Initialize the Response object with data from the JSON response.

        :param data: The JSON data parsed into a dictionary.
        """
        self.policyInfo = data.get('policyInfo')
        self.status = data.get('status')
        self.isGroup = data.get('isGroup')
        self.info = data.get('info')

    def __repr__(self) -> str:
        return f"<Response {self.__dict__}>"


class MinioadminMc:
    def __init__(self, databasename:str):
        """
        Initialize the MinioMc object with the database name.

        :param databasename: The name of the MinIO database.
        """
        self.databasename = databasename

    def removepolicy(self, policyname: str) -> Response:
        """
        Remove a policy from the MinIO database.

        :param policyname: The name of the policy to remove.
        :return: A Response object containing the result of the operation.
        """
        miniopolicyremovecommand = (
            f"mc admin policy rm --json {self.databasename} {policyname}"
        )
        output = subprocess.run(
            miniopolicyremovecommand, shell=True, capture_output=True, check=True
        )
        if output.returncode == 0:
            value = json.loads(output.stdout)
            return Response(value)
        else:
            raise Exception(f"Error {output.stderr.decode('utf-8')}")
    
    def getadmininfo(self) -> Response:
        miniocommand = f"mc admin info --json {self.databasename}"
        output = subprocess.run(miniocommand,shell=True,capture_output=True,check=True)
        if output.returncode == 0:
            value = json.loads(output.stdout)
            return Response(value)
        else:
            raise Exception(f"Error {output.stderr.decode('utf-8')}")
