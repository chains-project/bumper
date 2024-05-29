Here is a possible patch for the code:

```java
private org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DistributeReleaseBundleRequest createRequest(java.lang.String distRules, java.util.List<java.lang.String> countryCodes, java.lang.String siteName, java.lang.String cityName, boolean dryRun) throws java.io.IOException {
    org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DistributeReleaseBundleRequest request;
    if (org.apache.commons.lang3.StringUtils.isNotBlank(distRules)) {
        if ((!org.apache.commons.collections.CollectionUtils.isEmpty(countryCodes)) || (!org.apache.commons.lang3.StringUtils.isBlank(siteName) && !org.apache.commons.lang3.StringUtils.isBlank(cityName))) {
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

The change I made is to replace the method `isAllBlank` with two separate calls to `isBlank` in the following line:

```java
} else if ((!org.apache.commons.collections.CollectionUtils.isEmpty(countryCodes)) || (!org.apache.commons.lang3.StringUtils.isAllBlank(siteName, cityName))) {
```

This should fix the error because `isAllBlank` is not a method in the `StringUtils` class, but `isBlank` is. The `isAllBlank` method seems to be a custom method that checks if all the given strings are blank. To achieve the same functionality, I replaced it with a logical AND (`&&`) of two `isBlank` calls.

Note that I assumed that the intended behavior of the original code is to throw an exception if either `siteName` or `cityName` is not blank, so I used two separate `isBlank` calls. If the intended behavior is to throw an exception only if both `siteName` and `cityName` are not blank, then the code should be changed to:

```java
} else if ((!org.apache.commons.collections.CollectionUtils.isEmpty(countryCodes)) || (!org.apache.commons.lang3.StringUtils.isBlank(siteName) && !org.apache.commons.lang3.StringUtils.isBlank(cityName))) {
```

This change will throw an exception only if both `siteName` and `cityName` are not blank.