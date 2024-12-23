```java
public void execute() throws Exception {
    if (server == null) {
        throw new IllegalStateException("Artifactory server must be configured");
    }
    if ((kanikoImageFile == null || kanikoImageFile.trim().isEmpty()) && (jibImageFile == null || jibImageFile.trim().isEmpty()) || 
        (kanikoImageFile != null && !kanikoImageFile.trim().isEmpty()) && (jibImageFile != null && !jibImageFile.trim().isEmpty())) {
        throw new IllegalStateException("Exactly one of 'kanikoImageFile' or 'jibImageFile' must be configured");
    }
    CommonDeployer deployer = new CommonDeployer();
    deployer.setServer(server);
    deployer.setRepo(sourceRepo);
    FilePath tempDir = ExtractorUtils.createAndGetTempDir(ws);
    EnvExtractor envExtractor = new CreateDockerBuildEnvExtractor(build, buildInfo, deployer, listener, launcher, tempDir, env, kanikoImageFile, jibImageFile);
    super.execute("Create Docker Build", "org.jfrog.build.extractor.docker.extractor.BuildDockerCreator", envExtractor, tempDir);
}
```