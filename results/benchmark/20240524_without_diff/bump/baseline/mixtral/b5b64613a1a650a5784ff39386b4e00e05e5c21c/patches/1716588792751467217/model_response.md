Here's the proposed patch for the failing client code:

```java
private DeleteReleaseBundleRequest createRequest(String distRules, List<String> countryCodes, String siteName,
                                                 String cityName, boolean dryRun, boolean deleteFromDist) throws IOException {
    DeleteReleaseBundleRequest request = new DeleteReleaseBundleRequest();
    if (StringUtils.isNotBlank(distRules)) {
        ObjectMapper mapper = createMapper();
        request = mapper.readValue(distRules, DeleteReleaseBundleRequest.class);
    } else {
        request.setDistributionRules(Utils.createDistributionRules(countryCodes, siteName, cityName));
    }
    request.setDryRun(dryRun);
    request.setOnSuccess(deleteFromDist ?
            DeleteReleaseBundleRequest.OnSuccess.delete : DeleteReleaseBundleRequest.OnSuccess.keep);
    return request;
}
```

The change in the code is the addition of the `new DeleteReleaseBundleRequest()` on the first line of the method. This ensures that the `request` variable is always initialized, even when `distRules` is not blank, preventing the error message you encountered.