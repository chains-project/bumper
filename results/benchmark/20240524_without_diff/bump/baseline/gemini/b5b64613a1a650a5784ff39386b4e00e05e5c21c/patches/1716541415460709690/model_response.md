```java
import static org.apache.commons.lang3.StringUtils.isNotBlank;

public class CreateJFrogInstanceStep {

    public void perform(Run<?, ?> run, Launcher launcher, Variables variables, FilePath workspace, CreateJFrogInstanceStepDescriptor descriptor, JFrogInstance jfrogInstance) throws InterruptedException, IOException {
        if (jfrogInstance == null) {
            throw new IllegalArgumentException("JFrog instance cannot be null");
        }

        String artifactoryUrl = jfrogInstance.getUrl();
        if (isNotBlank(artifactoryUrl)) {
            variables.put("artifactoryUrl", artifactoryUrl);
        }

        String artifactoryUsername = jfrogInstance.getUsername();
        if (isNotBlank(artifactoryUsername)) {
            variables.put("artifactoryUsername", artifactoryUsername);
        }

        String artifactoryPassword = jfrogInstance.getPassword();
        if (isNotBlank(artifactoryPassword)) {
            variables.put("artifactoryPassword", artifactoryPassword);
        }

        String artifactoryToken = jfrogInstance.getToken();
        if (isNotBlank(artifactoryToken)) {
            variables.put("artifactoryToken", artifactoryToken);
        }

        String artifactoryProxy = jfrogInstance.getProxy();
        if (isNotBlank(artifactoryProxy)) {
            variables.put("artifactoryProxy", artifactoryProxy);
        }

        String artifactoryProxyUsername = jfrogInstance.getProxyUsername();
        if (isNotBlank(artifactoryProxyUsername)) {
            variables.put("artifactoryProxyUsername", artifactoryProxyUsername);
        }

        String artifactoryProxyPassword = jfrogInstance.getProxyPassword();
        if (isNotBlank(artifactoryProxyPassword)) {
            variables.put("artifactoryProxyPassword", artifactoryProxyPassword);
        }

        String artifactoryReleaseRepository = jfrogInstance.getReleaseRepository();
        if (isNotBlank(artifactoryReleaseRepository)) {
            variables.put("artifactoryReleaseRepository", artifactoryReleaseRepository);
        }

        String artifactorySnapshotRepository = jfrogInstance.getSnapshotRepository();
        if (isNotBlank(artifactorySnapshotRepository)) {
            variables.put("artifactorySnapshotRepository", artifactorySnapshotRepository);
        }

        String artifactoryVirtualRepository = jfrogInstance.getVirtualRepository();
        if (isNotBlank(artifactoryVirtualRepository)) {
            variables.put("artifactoryVirtualRepository", artifactoryVirtualRepository);
        }

        String artifactoryVirtualRepositoryLayout = jfrogInstance.getVirtualRepositoryLayout();
        if (isNotBlank(artifactoryVirtualRepositoryLayout)) {
            variables.put("artifactoryVirtualRepositoryLayout", artifactoryVirtualRepositoryLayout);
        }

        String artifactoryVirtualRepositoryPackageType = jfrogInstance.getVirtualRepositoryPackageType();
        if (isNotBlank(artifactoryVirtualRepositoryPackageType)) {
            variables.put("artifactoryVirtualRepositoryPackageType", artifactoryVirtualRepositoryPackageType);
        }

        String artifactoryVirtualRepositoryDefaultDeploymentRepository = jfrogInstance.getVirtualRepositoryDefaultDeploymentRepository();
        if (isNotBlank(artifactoryVirtualRepositoryDefaultDeploymentRepository)) {
            variables.put("artifactoryVirtualRepositoryDefaultDeploymentRepository", artifactoryVirtualRepositoryDefaultDeploymentRepository);
        }

        String artifactoryVirtualRepositoryDefaultReleaseRepository = jfrogInstance.getVirtualRepositoryDefaultReleaseRepository();
        if (isNotBlank(artifactoryVirtualRepositoryDefaultReleaseRepository)) {
            variables.put("artifactoryVirtualRepositoryDefaultReleaseRepository", artifactoryVirtualRepositoryDefaultReleaseRepository);
        }

        String artifactoryVirtualRepositoryDefaultSnapshotRepository = jfrogInstance.getVirtualRepositoryDefaultSnapshotRepository();
        if (isNotBlank(artifactoryVirtualRepositoryDefaultSnapshotRepository)) {
            variables.put("artifactoryVirtualRepositoryDefaultSnapshotRepository", artifactoryVirtualRepositoryDefaultSnapshotRepository);
        }

        String artifactoryVirtualRepositoryPropertySets = jfrogInstance.getVirtualRepositoryPropertySets();
        if (isNotBlank(artifactoryVirtualRepositoryPropertySets)) {
            variables.put("artifactoryVirtualRepositoryPropertySets", artifactoryVirtualRepositoryPropertySets);
        }

        String artifactoryVirtualRepositoryKey = jfrogInstance.getVirtualRepositoryKey();
        if (isNotBlank(artifactoryVirtualRepositoryKey)) {
            variables.put("artifactoryVirtualRepositoryKey", artifactoryVirtualRepositoryKey);
        }

        String artifactoryVirtualRepositoryNotes = jfrogInstance.getVirtualRepositoryNotes();
        if (isNotBlank(artifactoryVirtualRepositoryNotes)) {
            variables.put("artifactoryVirtualRepositoryNotes", artifactoryVirtualRepositoryNotes);
        }

        String artifactoryVirtualRepositoryIncludesPattern = jfrogInstance.getVirtualRepositoryIncludesPattern();
        if (isNotBlank(artifactoryVirtualRepositoryIncludesPattern)) {
            variables.put("artifactoryVirtualRepositoryIncludesPattern", artifactoryVirtualRepositoryIncludesPattern);
        }

        String artifactoryVirtualRepositoryExcludesPattern = jfrogInstance.getVirtualRepositoryExcludesPattern();
        if (isNotBlank(artifactoryVirtualRepositoryExcludesPattern)) {
            variables.put("artifactoryVirtualRepositoryExcludesPattern", artifactoryVirtualRepositoryExcludesPattern);
        }

        String artifactoryVirtualRepositoryMaxUniqueSnapshots = jfrogInstance.getVirtualRepositoryMaxUniqueSnapshots();
        if (isNotBlank(artifactoryVirtualRepositoryMaxUniqueSnapshots)) {
            variables.put("artifactoryVirtualRepositoryMaxUniqueSnapshots", artifactoryVirtualRepositoryMaxUniqueSnapshots);
        }

        String artifactoryVirtualRepositorySnapshotVersionBehavior = jfrogInstance.getVirtualRepositorySnapshotVersionBehavior();
        if (isNotBlank(artifactoryVirtualRepositorySnapshotVersionBehavior)) {
            variables.put("artifactoryVirtualRepositorySnapshotVersionBehavior", artifactoryVirtualRepositorySnapshotVersionBehavior);
        }

        String artifactoryVirtualRepositorySuppressPomConsistencyChecks = jfrogInstance.getVirtualRepositorySuppressPomConsistencyChecks();
        if (isNotBlank(artifactoryVirtualRepositorySuppressPomConsistencyChecks)) {
            variables.put("artifactoryVirtualRepositorySuppressPomConsistencyChecks", artifactoryVirtualRepositorySuppressPomConsistencyChecks);
        }

        String artifactoryVirtualRepositoryHandleReleases = jfrogInstance.getVirtualRepositoryHandleReleases();
        if (isNotBlank(artifactoryVirtualRepositoryHandleReleases)) {
            variables.put("artifactoryVirtualRepositoryHandleReleases", artifactoryVirtualRepositoryHandleReleases);
        }

        String artifactoryVirtualRepositoryBlackedOut = jfrogInstance.getVirtualRepositoryBlackedOut();
        if (isNotBlank(artifactoryVirtualRepositoryBlackedOut)) {
            variables.put("artifactoryVirtualRepositoryBlackedOut", artifactoryVirtualRepositoryBlackedOut);
        }

        String artifactoryVirtualRepositoryPropertySetsIncludePatterns = jfrogInstance.getVirtualRepositoryPropertySetsIncludePatterns();
        if (isNotBlank(artifactoryVirtualRepositoryPropertySetsIncludePatterns)) {
            variables.put("artifactoryVirtualRepositoryPropertySetsIncludePatterns", artifactoryVirtualRepositoryPropertySetsIncludePatterns);
        }

        String artifactoryVirtualRepositoryPropertySetsExcludePatterns = jfrogInstance.getVirtualRepositoryPropertySetsExcludePatterns();
        if (isNotBlank(artifactoryVirtualRepositoryPropertySetsExcludePatterns)) {
            variables.put("artifactoryVirtualRepositoryPropertySetsExcludePatterns", artifactoryVirtualRepositoryPropertySetsExcludePatterns);
        }

        String artifactoryVirtualRepositoryPropertySetsOverrideExisting = jfrogInstance.getVirtualRepositoryPropertySetsOverrideExisting();
        if (isNotBlank(artifactoryVirtualRepositoryPropertySetsOverrideExisting)) {
            variables.put("artifactoryVirtualRepositoryPropertySetsOverrideExisting", artifactoryVirtualRepositoryPropertySetsOverrideExisting);
        }

        String artifactoryVirtualRepositoryPropertySetsAppend = jfrogInstance.getVirtualRepositoryPropertySetsAppend();
        if (isNotBlank(artifactoryVirtualRepositoryPropertySetsAppend)) {
            variables.put("artifactoryVirtualRepositoryPropertySetsAppend", artifactoryVirtualRepositoryPropertySetsAppend);
        }
    }
}
```