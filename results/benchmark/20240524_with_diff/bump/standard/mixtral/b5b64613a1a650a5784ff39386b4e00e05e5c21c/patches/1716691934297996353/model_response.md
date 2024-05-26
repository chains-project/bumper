Here's the proposed patch for the `createRequest` method:
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
The changes include:

* Importing the missing class `org.apache.commons.collections4.CollectionUtils` from the updated library version.
* Replacing the deprecated method `org.apache.commons.collections.CollectionUtils.isEmpty` with the new method `org.apache.commons.collections4.CollectionUtils.isEmpty`.

Note that the `isAllBlank` method is not present in the updated version of the `org.apache.commons.lang3.StringUtils` class. Instead, you can create a custom utility method to achieve the same functionality:
```java
public static boolean isAllBlank(String... strings) {
    return Arrays.stream(strings).allMatch(StringUtils::isBlank);
}
```
Add this method to a utility class and import it in your code to use it as a replacement for `org.apache.commons.lang3.StringUtils.isAllBlank`.