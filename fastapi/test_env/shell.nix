{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (ps: [
      ps.flask
      ps.fastapi
      ps.pylsp-mypy
      ps.pip
    ]))

    pkgs.curl
    pkgs.jq
  ];
}