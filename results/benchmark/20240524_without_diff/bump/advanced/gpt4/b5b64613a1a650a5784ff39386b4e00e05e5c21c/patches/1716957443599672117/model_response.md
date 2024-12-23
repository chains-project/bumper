```java
public void execute() throws java.lang.Exception {
    if (server == null) {
        throw new java.lang.IllegalStateException("Artifactory server must be configured");
    }
    if ((org.apache.commons.lang3.StringUtils.isBlank(kanikoImageFile) && org.apache.commons.lang3.StringUtils.isBlank(jibImageFile)) || (!org.apache.commons.lang3.StringUtils.isBlank(kanikoImageFile) && !org.apache.commons.lang3.StringUtils.isBlank(jibImageFile))) {
        throw new java.lang.IllegalStateException("Exactly one of 'kanikoImageFile' or 'jibImageFile' must be configured");
    }
    org.jfrog.hudson.pipeline.common.types.deployers.CommonDeployer deployer = new org.jfrog.hudson.pipeline.common.types.deployers.CommonDeployer();
    deployer.setServer(server);
    deployer.setRepo(sourceRepo);
    hudson.FilePath tempDir = org.jfrog.hudson.util.ExtractorUtils.createAndGetTempDir(ws);
    org.jfrog.hudson.pipeline.common.executors.EnvExtractor envExtractor = new org.jfrog.hudson.pipeline.common.executors.CreateDockerBuildEnvExtractor(build, buildInfo, deployer, listener, launcher, tempDir, env, kanikoImageFile, jibImageFile);
    super.execute("Create Docker Build", "org.jfrog.build.extractor.docker.extractor.BuildDockerCreator", envExtractor, tempDir);
}
```