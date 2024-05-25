```java
  @Test
    void shouldPush() throws Exception {
        final Image original = new Image.ForOs();
        final String image = this.copy(original);
        final String output = this.cli.run("push", image);
        final String expectedDigest = String.format("latest: digest: %s", original.digest());
        assertThat(output, containsString(expectedDigest));
    }
```