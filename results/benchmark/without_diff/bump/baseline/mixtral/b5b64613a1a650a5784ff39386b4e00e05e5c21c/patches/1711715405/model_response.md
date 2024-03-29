Here is a fixed version of the `createRequest` method that should resolve the error:
```java
private DeleteReleaseBundleRequest createRequest(String distRules, List<String> countryCodes, String siteName,
                                                 String cityName, boolean dryRun, boolean deleteFromDist) throws IOException {
    DeleteReleaseBundleRequest.DeleteReleaseBundleRequestBuilder requestBuilder = DeleteReleaseBundleRequest.builder();

    if (StringUtils.isNotBlank(distRules)) {
        if (!CollectionUtils.isEmpty(countryCodes) || !StringUtils.isAllBlank(siteName, cityName)) {
            throw new IOException("The distRules input can't be used with site, city or country codes");
        }
        ObjectMapper mapper = createMapper();
        requestBuilder.distributionRules(mapper.readValue(distRules, DeleteReleaseBundleRequest.class).getDistributionRules());
    } else {
        requestBuilder.distributionRules(Utils.createDistributionRules(countryCodes, siteName, cityName));
    }

    requestBuilder.dryRun(dryRun);
    requestBuilder.onSuccess(deleteFromDist ?
            DeleteReleaseBundleRequest.OnSuccess.DELETE : DeleteReleaseBundleRequest.OnSuccess.KEEP);

    return requestBuilder.build();
}
```
The main change is that instead of directly modifying the `request` object, we are now using the `DeleteReleaseBundleRequest.DeleteReleaseBundleRequestBuilder` class to create a request builder, and then using that builder to create the final request object. This allows us to avoid directly modifying the `request` object, which was causing the "cannot find symbol" error.

I also changed the `onSuccess` field to use the enum constants in uppercase, as indicated by the `++` in the prompt.

Note that this code assumes that the `createMapper` method used in the original code has not been changed, and that the `Utils.createDistributionRules` method has not been removed. If either of these assumptions is incorrect, additional changes may be necessary.