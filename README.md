# Bump-ER
Automatic repair for breaking dependency update (bump)

# Findings
- Some clients fail because the new dependency version required a different java version
  - those clients are not easy to fix as they required a major update of java version, so they are `skipped`.
- dependencyGroupID (in bump .json files) is extracted from the pom.xml file, but is not always equal to the package id.
  - this means it CANNOT be safely used to identifying breaking changes within "breaking good" project
  - E.G.: [4a3efad6e00824e5814b9c8f571c9c98aad40281](benchmarks/bump/repository/data/benchmark/4a3efad6e00824e5814b9c8f571c9c98aad40281.json)
    - `depencencyGroupID = "eu.europa.ec.joinup.sd-dss"` while most packages are `eu.europa.esig.dss`
- For `cannot find symbol` the error could point directly to the import line.
  - in this case our FL based on Spoon, cannot find the correct method (there is none, error is in import)
  - Also, prompt template needs to be different


# Others
## BUMP
- [78 clients](./benchmarks/bump/analysis/clients_failing_due_to_java_version.txt) have failures due to incompatible java version, they won't be used with the repair pipeline
- [141 clients](./benchmarks/bump/analysis/clients_failing_due_to_internal_apis.txt) have failures due to usage of internal api, they won't be used with the repair pipeline