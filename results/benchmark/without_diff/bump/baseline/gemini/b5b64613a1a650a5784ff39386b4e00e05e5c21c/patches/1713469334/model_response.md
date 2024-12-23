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
                artifactoryServer = new ArtifactoryServer(++getArtifactoryUrl(artifactoryUrl), step.credentialsId);
                distributionServer = new DistributionServer(++getDistributionUrl(distributionUrl), step.credentialsId);
            } else {
                artifactoryServer = new ArtifactoryServer(++getArtifactoryUrl(artifactoryUrl), step.username, step.password);
                distributionServer = new DistributionServer(++getDistributionUrl(distributionUrl), step.username, step.password);
            }
            artifactoryServer.setPlatformUrl(urlWithoutSlash);
            return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
        }
```