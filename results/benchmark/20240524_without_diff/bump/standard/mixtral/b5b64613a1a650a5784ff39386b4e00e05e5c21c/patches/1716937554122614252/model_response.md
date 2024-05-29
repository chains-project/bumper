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
    for (String str : strings) {
        if (org.apache.commons.lang3.StringUtils.isNotBlank(str)) {
            return false;
        }
    }
    return true;
}
```

In this version, I added a new private method `isAllBlank` that takes a variable number of `String` arguments and checks if all of them are blank using the `org.apache.commons.lang3.StringUtils.isNotBlank` method. This method can be used as a replacement for the missing `org.apache.commons.lang3.StringUtils.isAllBlank` method.