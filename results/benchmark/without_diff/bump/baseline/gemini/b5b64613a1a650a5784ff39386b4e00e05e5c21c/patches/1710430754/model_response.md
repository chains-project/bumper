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
                artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.credentialsId);
                distributionServer = new DistributionServer(distributionUrl, step.credentialsId);
            } else if (!isEmpty(step.username) && !isEmpty(step.password)) {
                artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.username, step.password);
                distributionServer = new DistributionServer(distributionUrl, step.username, step.password);
            } else {
                throw new IllegalArgumentException("Either 'credentialsId' or both 'username' and 'password' must be specified");
            }
            artifactoryServer.setPlatformUrl(urlWithoutSlash);
            return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
        }
```