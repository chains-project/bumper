```java
  private DeleteReleaseBundleRequest createRequest(String distRules, List<String> countryCodes, String siteName,
                                                     String cityName, boolean dryRun, boolean deleteFromDist) throws IOException {
        if (StringUtils.isNotBlank(distRules) && (!CollectionUtils.isEmpty(countryCodes) || !StringUtils.isAllBlank(siteName, cityName))) {
            throw new IOException("The distRules input can't be used with site, city or country codes");
        }

        ObjectMapper mapper = createMapper();
        DeleteReleaseBundleRequest request = mapper.readValue(distRules, DeleteReleaseBundleRequest.class);
        request.setDryRun(dryRun);
        request.setOnSuccess(deleteFromDist ?
                DeleteReleaseBundleRequest.OnSuccess.delete : DeleteReleaseBundleRequest.OnSuccess.keep);
        return request;
    }
```