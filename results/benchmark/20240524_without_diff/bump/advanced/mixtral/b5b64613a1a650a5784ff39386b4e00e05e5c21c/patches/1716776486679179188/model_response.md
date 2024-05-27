Here is a possible patch for the given code:

```java
private org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest createRequest(java.lang.String distRules, java.util.List<java.lang.String> countryCodes, java.lang.String siteName, java.lang.String cityName, boolean dryRun, boolean deleteFromDist) throws java.io.IOException {
    org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest request;
    if (org.apache.commons.lang3.StringUtils.isNotBlank(distRules)) {
        if ((!org.apache.commons.collections.CollectionUtils.isEmpty(countryCodes)) || (!org.apache.commons.lang3.StringUtils.isBlank(siteName) && !org.apache.commons.lang3.StringUtils.isBlank(cityName))) {
            throw new java.io.IOException("The distRules input can't be used with site, city or country codes");
        }
        com.fasterxml.jackson.databind.ObjectMapper mapper = SerializationUtils.createMapper();
        request = mapper.readValue(distRules, org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest.class);
    } else {
        request = new org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest();
        request.setDistributionRules(org.jfrog.hudson.pipeline.common.Utils.createDistributionRules(countryCodes, siteName, cityName));
    }
    request.setDryRun(dryRun);
    request.setOnSuccess(deleteFromDist ? DeleteReleaseBundleRequest.OnSuccess.delete : DeleteReleaseBundleRequest.OnSuccess.keep);
    return request;
}
```

The patch changes the line that uses `isAllBlank` method to use `isBlank` method instead, and checks the two strings separately. This is because the `isAllBlank` method does not exist in the `StringUtils` class of the `org.apache.commons.lang3` package, but the `isBlank` method does.

The `isAllBlank` method is not a standard method in the `StringUtils` class, but it can be easily implemented using the `isBlank` method as follows:

```java
public static boolean isAllBlank(String... strs) {
    for (String str : strs) {
        if (!isBlank(str)) {
            return false;
        }
    }
    return true;
}
```

However, since the patch should only modify the client code and not the external dependencies, the above implementation should be added to the external dependency if needed.