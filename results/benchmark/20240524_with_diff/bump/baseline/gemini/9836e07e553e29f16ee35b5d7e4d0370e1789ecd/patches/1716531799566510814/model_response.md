```java
@Test
    void shouldPush() throws Exception {
        final Image original = new Image.ForOs();
        final String image = this.copy(original);
        final String output = this.cli.run("push", image);
        MatcherAssert.assertThat(
            output,
            containsString(String.format("latest: digest: %s", original.digest()))
        );
    }
```