Here's a modified version of the `createRequest` method that should fix the error:

```java
private DeleteReleaseBundleRequest createRequest(String distRules, List<String> countryCodes, String siteName,
                                                 String cityName, boolean dryRun, boolean deleteFromDist) throws IOException {
    DeleteReleaseBundleRequest.DeleteReleaseBundleRequestBuilder requestBuilder = DeleteReleaseBundleRequest.builder();

    if (StringUtils.isNotBlank(distRules)) {
        if (!CollectionUtils.isEmpty(countryCodes) || !StringUtils.isAllBlank(siteName, cityName)) {
            throw new IOException("The distRules input can't be used with site, city or country codes");
        }
        ObjectMapper mapper = createMapper();
        DeleteReleaseBundleRequest request = mapper.readValue(distRules, DeleteReleaseBundleRequest.class);
        requestBuilder.distributionRules(request.getDistributionRules());
    } else {
        requestBuilder.distributionRules(Utils.createDistributionRules(countryCodes, siteName, cityName));
    }

    requestBuilder.dryRun(dryRun);
    requestBuilder.onSuccess(deleteFromDist ?
            DeleteReleaseBundleRequest.OnSuccess.DELETE : DeleteReleaseBundleRequest.OnSuccess.KEEP);

    return requestBuilder.build();
}
```

The changes made include:

* Using the `DeleteReleaseBundleRequest.builder()` method to create a new `DeleteReleaseBundleRequest` instance, instead of directly instantiating it with `new`.
* Using the `DeleteReleaseBundleRequest.builder()` method to set each property of the request, instead of directly setting them on the request instance.
* Using the `DELETE` and `KEEP` constants on the `DeleteReleaseBundleRequest.OnSuccess` enum, instead of the string literals `"delete"` and `"keep"`.

These changes should resolve the "cannot find symbol" error, by avoiding the use of any removed library methods or classes.