Here's a suggested patch for the given code. It appears that the error is related to the `createMapper()` method call, which is not provided in the code snippet. I'm assuming it is a Jackson `ObjectMapper` instance creation.

```java
private DeleteReleaseBundleRequest createRequest(String distRules, List<String> countryCodes, String siteName,
                                                 String cityName, boolean dryRun, boolean deleteFromDist) throws IOException {
    DeleteReleaseBundleRequest request;
    ObjectMapper mapper = new ObjectMapper(); // Added
    if (StringUtils.isNotBlank(distRules)) {
        if (!CollectionUtils.isEmpty(countryCodes) || !StringUtils.isAllBlank(siteName, cityName)) {
            throw new IOException("The distRules input can't be used with site, city or country codes");
        }
        request = mapper.readValue(distRules, DeleteReleaseBundleRequest.class);
    } else {
        request = new DeleteReleaseBundleRequest();
        request.setDistributionRules(Utils.createDistributionRules(countryCodes, siteName, cityName));
    }
    request.setDryRun(dryRun);
    request.setOnSuccess(deleteFromDist ?
            DeleteReleaseBundleRequest.OnSuccess.delete : DeleteReleaseBundleRequest.OnSuccess.keep);
    return request;
}
```

This patch initializes the `ObjectMapper` instance directly in the method, assuming the `createMapper()` method was merely a factory method for creating an `ObjectMapper`. If the `createMapper()` method contained additional logic, please adjust the code accordingly.