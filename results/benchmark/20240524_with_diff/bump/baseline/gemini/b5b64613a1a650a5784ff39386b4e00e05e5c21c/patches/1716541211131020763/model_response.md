```java
  protected JFrogPlatformInstance run() throws Exception {
            if (StringUtils.isBlank(step.url) && StringUtils.isBlank(step.artifactoryUrl) && StringUtils.isBlank(step.distributionUrl)) {
                throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
            }
            String urlWithoutSlash = StringUtils.removeEnd(step.url, "/");
            String artifactoryUrl = StringUtils.defaultIfBlank(step.artifactoryUrl, urlWithoutSlash + "/" + "artifactory");
            String distributionUrl = StringUtils.defaultIfBlank(step.distributionUrl, urlWithoutSlash + "/" + "distribution");

            ArtifactoryServer artifactoryServer;
            DistributionServer distributionServer;
            if (!StringUtils.isBlank(step.credentialsId)) {
                artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.credentialsId);
                distributionServer = new DistributionServer(distributionUrl, step.credentialsId);
            } else {
                artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.username, step.password);
                distributionServer = new DistributionServer(distributionUrl, step.username, step.password);
            }
            artifactoryServer.setPlatformUrl(urlWithoutSlash);
            return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
        }
```