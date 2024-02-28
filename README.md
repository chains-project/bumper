# Bump-ER
Automatic repair for breaking dependency update (bump)

# Findings
- dependencyGroupID (in bump .json files) is extracted from the pom.xml file, but is not always equal to the package id.
  - this means it CANNOT be safely used to identifying breaking changes within "breaking good" project
  - E.G.: [4a3efad6e00824e5814b9c8f571c9c98aad40281](benchmarks/bump/repository/data/benchmark/4a3efad6e00824e5814b9c8f571c9c98aad40281.json)
    - `depencencyGroupID = "eu.europa.ec.joinup.sd-dss"` while most packages are `eu.europa.esig.dss`