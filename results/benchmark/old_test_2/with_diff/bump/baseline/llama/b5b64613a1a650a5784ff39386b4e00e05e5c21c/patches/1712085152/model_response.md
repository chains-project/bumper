```
  // TODO: review this AI generated patch!
if (step.url == null || step.artifactoryUrl == null || step.distributionUrl == null) {
    throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
}

if (isEmpty(step.url) || isEmpty(step.artifactoryUrl) || isEmpty(step.distributionUrl)) {
    throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
}
```

change `isEmpty()` to `isNullOrEmpty()`

```
  // TODO: review this AI generated patch!
if (step.url == null || step.artifactoryUrl == null || step.distributionUrl == null) {
    throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
}

if (step.url == null || step.artifactoryUrl == null || step.distributionUrl == null) {
    throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
}
```

Also, you can remove the `Override` decorator as it is not needed.