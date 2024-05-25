```java
  @Override
        protected JFrogPlatformInstance run() throws Exception {
            if (isAllBlank(step.url, step.artifactoryUrl, step.distributionUrl)) {
                throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
            }
            String urlWithoutSlash = removeEnd(step.url, "/");
            String artifactoryUrl = defaultIfBlank(step.artifactoryUrl, urlWithoutSlash + "/" + "artifactory");
            String distributionUrl = defaultIfBlank(step.distributionUrl, urlWithoutSlash + "/" + "distribution");

            // Create ArtifactoryServer and DistributionServer instances
            ArtifactoryServer artifactoryServer;
            DistributionServer distributionServer;

            // Check if credentialsId is provided
            if (!isEmpty(step.credentialsId)) {
                artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.credentialsId);
                distributionServer = new DistributionServer(distributionUrl, step.credentialsId);
            } else {
                // If credentialsId is not provided, use username and password
                artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.username, step.password);
                distributionServer = new DistributionServer(distributionUrl, step.username, step.password);
            }

            // Set platform URL for ArtifactoryServer
            artifactoryServer.setPlatformUrl(urlWithoutSlash);

            // Create JFrogPlatformInstance and return it
            return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
        }
```