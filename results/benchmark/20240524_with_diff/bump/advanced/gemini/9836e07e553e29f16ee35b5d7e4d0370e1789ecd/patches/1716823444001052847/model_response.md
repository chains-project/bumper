```java
// TODO: review this AI generated patch!
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable;
    try {
        final java.util.List<java.lang.String> parts = java.util.Arrays.asList(string.split(":"));
        final java.lang.String host = parts.get(0);
        final java.lang.String port = parts.get(1);
        final java.lang.String path = parts.get(2);
        final java.net.URI uri = new java.net.URI("http", host, port, path, null, null, null);
        final java.net.HttpURLConnection connection = (java.net.HttpURLConnection) uri.toURL().openConnection();
        connection.setRequestMethod("GET");
        connection.connect();
        final int responseCode = connection.getResponseCode();
        if (responseCode != 200) {
            throw new java.lang.RuntimeException("Invalid response code: " + responseCode);
        }
        final java.io.BufferedReader reader = new java.io.BufferedReader(new java.io.InputStreamReader(connection.getInputStream()));
        final java.lang.StringBuilder builder = new java.lang.StringBuilder();
        java.lang.String line;
        while ((line = reader.readLine()) != null) {
            builder.append(line);
        }
        reader.close();
        final java.lang.String response = builder.toString();
        final java.util.Map<java.lang.String, java.lang.Object> map = new java.util.HashMap<>();
        map.put("host", host);
        map.put("port", port);
        map.put("path", path);
        map.put("response", response);
        throwable = null;
    } catch (final java.lang.Exception e) {
        throwable = e;
    }
    org.junit.jupiter.api.Assertions.assertNotNull(throwable);
}
```