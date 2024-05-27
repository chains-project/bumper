Here's the proposed patch for the `createRequest` method to fix the error:
```java
private org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest createRequest(java.lang.String distRules, java.util.List<java.lang.String> countryCodes, java.lang.String siteName, java.lang.String cityName, boolean dryRun, boolean deleteFromDist) throws java.io.IOException {
    org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest request;
    if (org.apache.commons.lang3.StringUtils.isNotBlank(distRules)) {
        if ((!org.apache.commons.collections4.CollectionUtils.isEmpty(countryCodes)) || (!org.apache.commons.lang3.StringUtils.isAllBlank(siteName, cityName))) {
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
In this patch, I replaced the deprecated `org.apache.commons.collections.CollectionUtils.isEmpty` method with `org.apache.commons.collections4.CollectionUtils.isEmpty` method. This should fix the error.

Additionally, I noticed that the `isAllBlank` method is not present in the `org.apache.commons.lang3.StringUtils` class. Instead, you can use the following code snippet to achieve the same functionality:
```java
public static boolean isAllBlank(String... strings) {
    for (String string : strings) {
        if (StringUtils.isNotBlank(string)) {
            return false;
        }
    }
    return true;
}
```
You can add this method to a utility class and use it in your code. This should fix the error.