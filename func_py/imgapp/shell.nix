{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (ps: with ps; [
      # Just MacOS things - need overriding to skip tests with module calls
      (pylsp-mypy.overridePythonAttrs (_: { doCheck = false; }))
    ]))

    pkgs.curl
    pkgs.jq
  ];

  buildInputs = [
    pkgs.python3
    pkgs.poetry
  ];
}