{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (ps: with ps; [
      flask
      fastapi
      # Just MacOS things - need overriding to skip tests with module calls
      (pylsp-mypy.overridePythonAttrs (_: { doCheck = false; }))
      pip
      uvicorn
    ]))

    pkgs.curl
    pkgs.jq
  ];
}