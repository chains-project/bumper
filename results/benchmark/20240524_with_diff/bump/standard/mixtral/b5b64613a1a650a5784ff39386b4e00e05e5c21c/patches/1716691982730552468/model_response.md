Here's the patched method:
```java
private org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest createRequest(java.lang.String distRules, java.util.List<java.lang.String> countryCodes, java.lang.String siteName, java.lang.String cityName, boolean dryRun, boolean deleteFromDist) throws java.io.IOException {
    org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest request;
    if (org.apache.commons.lang3.StringUtils.isNotBlank(distRules)) {
        if ((!org.apache.commons.collections.CollectionUtils.isEmpty(countryCodes)) || (org.apache.commons.lang3.StringUtils.isNotBlank(siteName) && org.apache.commons.lang3.StringUtils.isNotBlank(cityName))) {
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
The only change I made is in the condition:
```java
(!org.apache.commons.collections.CollectionUtils.isEmpty(countryCodes)) || (!org.apache.commons.lang3.StringUtils.isAllBlank(siteName, cityName))
```
was replaced with:
```java
(!org.apache.commons.collections.CollectionUtils.isEmpty(countryCodes)) || (org.apache.commons.lang3.StringUtils.isNotBlank(siteName) && org.apache.commons.lang3.StringUtils.isNotBlank(cityName))
```
Because `isAllBlank` is not available anymore, this change checks if both `siteName` and `cityName` are not blank, instead of checking if they are both blank.