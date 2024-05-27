Here's a fixed version of the `createRequest` method that uses `org.apache.commons.lang3.StringUtils.isAnyBlank` instead of the removed `isAllBlank` method:

```java
private org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DistributeReleaseBundleRequest createRequest(java.lang.String distRules, java.util.List<java.lang.String> countryCodes, java.lang.String siteName, java.lang.String cityName, boolean dryRun) throws java.io.IOException {
    org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DistributeReleaseBundleRequest request;
    if (org.apache.commons.lang3.StringUtils.isNotBlank(distRules)) {
        if ((!org.apache.commons.collections.CollectionUtils.isEmpty(countryCodes)) || (org.apache.commons.lang3.StringUtils.isAnyBlank(siteName, cityName))) {
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
```
The only change made is replacing the line `if (!org.apache.commons.lang3.StringUtils.isAllBlank(siteName, cityName)) {` with `if (org.apache.commons.lang3.StringUtils.isAnyBlank(siteName, cityName)) {`. This is because the `isAllBlank` method has been removed from the updated library version. Instead, we can use the `isAnyBlank` method to check if either `siteName` or `cityName` is blank.