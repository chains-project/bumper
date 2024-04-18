Here is a fixed version of the `createRequest` method that should resolve the "cannot find symbol" error:

```java
private DeleteReleaseBundleRequest createRequest(String distRules, List<String> countryCodes, String siteName,
                                                 String cityName, boolean dryRun, boolean deleteFromDist) throws IOException {
    DeleteReleaseBundleRequest.DeleteReleaseBundleRequestBuilder requestBuilder = DeleteReleaseBundleRequest.builder();

    if (StringUtils.isNotBlank(distRules)) {
        if (!CollectionUtils.isEmpty(countryCodes) || !StringUtils.isAllBlank(siteName, cityName)) {
            throw new IOException("The distRules input can't be used with site, city or country codes");
        }
        ObjectMapper mapper = createMapper();
        requestBuilder.distributionRules(mapper.readValue(distRules, DistributionRules.class));
    } else {
        requestBuilder.distributionRules(Utils.createDistributionRules(countryCodes, siteName, cityName));
    }

    requestBuilder.dryRun(dryRun);
    requestBuilder.onSuccess(deleteFromDist ?
            DeleteReleaseBundleRequest.OnSuccess.DELETE : DeleteReleaseBundleRequest.OnSuccess.KEEP);

    return requestBuilder.build();
}
```

This version of the method uses the `DeleteReleaseBundleRequest.DeleteReleaseBundleRequestBuilder` class to build the `DeleteReleaseBundleRequest` object. This allows us to set the properties of the request object in a fluent and type-safe way, avoiding the need to use raw types and casts.

Additionally, I have changed the `OnSuccess` enum values to their all-uppercase equivalents, as this is the convention used in the rest of the code.

Note that I had to make some assumptions about the `createMapper` and `createDistributionRules` methods, as they were not provided in the original code snippet. I assumed that `createMapper` returns an `ObjectMapper` instance and that `createDistributionRules` returns a `DistributionRules` instance, as these are the types that are expected by the `DeleteReleaseBundleRequest.builder()` method. If these assumptions are incorrect, the code may need to be adjusted accordingly.