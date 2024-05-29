Here's a fixed version of the `createRequest` method that replaces the `org.apache.commons.lang3.StringUtils.isAllBlank` method with an equivalent implementation using the `org.apache.commons.lang3.StringUtils.isBlank` method:

```java
private org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DistributeReleaseBundleRequest createRequest(java.lang.String distRules, java.util.List<java.lang.String> countryCodes, java.lang.String siteName, java.lang.String cityName, boolean dryRun) throws java.io.IOException {
    org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DistributeReleaseBundleRequest request;
    if (org.apache.commons.lang3.StringUtils.isNotBlank(distRules)) {
        if ((!org.apache.commons.collections.CollectionUtils.isEmpty(countryCodes)) || (!isAllBlank(siteName, cityName))) {
            throw new java.io.IOException("The distRules input can't be used with site, city or country codes");
        }
        com.fasterxml.jackson.databind.ObjectMapper mapper = SerializationUtils.createMapper();
        request = mapper.readValue(distRules, org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DistributeReleaseBundleRequest.class);
    } else {
        request = new org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DistributeReleaseBundleRequest();
        request.setDistributionRules(org.jfrog.hudson.pipeline.common.Utils.createDistributionRules(countryCodes, siteName, cityName));
    }
    request.setDryRun(dryRun);
    return request;
}

private boolean isAllBlank(String... strings) {
    for (String string : strings) {
        if (org.apache.commons.lang3.StringUtils.isNotBlank(string)) {
            return false;
        }
    }
    return true;
}
```

This implementation defines a new `isAllBlank` method that takes a variable number of `String` arguments and checks if all of them are blank. It uses the `org.apache.commons.lang3.StringUtils.isNotBlank` method to check if a string is not blank, and returns `true` if all strings are blank, and `false` otherwise.