```java
private DistributeReleaseBundleRequest createRequest(String distRules, List<String> countryCodes,
                                                         String siteName, String cityName, boolean dryRun) throws IOException {
    DistributeReleaseBundleRequest request;
    if (StringUtils.isNotBlank(distRules)) {
        if (!CollectionUtils.isEmpty(countryCodes) || !StringUtils.isBlank(siteName) || !StringUtils.isBlank(cityName)) {
            throw new IOException("The distRules input can't be used with site, city or country codes");
        }
        ObjectMapper mapper = createMapper();
        request = mapper.readValue(distRules, DistributeReleaseBundleRequest.class);
    } else {
        request = new DistributeReleaseBundleRequest();
        request.setDistributionRules(Utils.createDistributionRules(countryCodes, siteName, cityName));
    }
    request.setDryRun(dryRun);
    return request;
}
``` 
