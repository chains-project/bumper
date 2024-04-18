Here's a proposed patch to fix the error:
```java
  @Override
        protected JFrogPlatformInstance run() throws Exception {
            if (isAllBlank(step.url, step.artifactoryUrl, step.distributionUrl)) {
                throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
            }
            String urlWithoutSlash = removeEnd(step.url, "/");
            String artifactoryUrl = defaultIfBlank(step.artifactoryUrl, urlWithoutSlash + "/" + "artifactory");
            String distributionUrl = defaultIfBlank(step.distributionUrl, urlWithoutSlash + "/" + "distribution");

            ArtifactoryServer artifactoryServer;
            DistributionServer distributionServer;
            if (!isEmpty(step.credentialsId)) {
                artifactoryServer = new ArtifactoryServerImpl(urlWithoutSlash, step.credentialsId);
                distributionServer = new DistributionServerImpl(distributionUrl, step.credentialsId);
            } else {
                artifactoryServer = new ArtifactoryServerImpl(artifactoryUrl, step.username, step.password);
                distributionServer = new DistributionServerImpl(distributionUrl, step.username, step.password);
            }
            artifactoryServer.setPlatformUrl(urlWithoutSlash);
            return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
        }
```
The changes made are:

* Replace the constructor of `ArtifactoryServer` and `DistributionServer` with the new constructor `ArtifactoryServerImpl` and `DistributionServerImpl` respectively, which are added in the new version.
* Remove the `--` and `++` symbols, as they are not needed and may cause confusion.

Note: The solution assumes that the `ArtifactoryServerImpl` and `DistributionServerImpl` classes are available in the new version of the external dependency and have the same functionality as the old versions.