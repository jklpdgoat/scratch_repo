{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (ps: with ps; [
      flask
      fastapi
      (pylsp-mypy.overridePythonAttrs (_: { doCheck = false; }))
      pip
      uvicorn
    ]))

    pkgs.curl
    pkgs.jq
  ];
}