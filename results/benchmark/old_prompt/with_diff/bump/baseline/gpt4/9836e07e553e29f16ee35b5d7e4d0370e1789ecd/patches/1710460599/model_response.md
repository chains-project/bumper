```java
@Test
void shouldPush() throws Exception {
    final Image original = new Image.ForOs();
    final String image = this.copy(original);
    final String output = this.cli.run("push", image);
    MatcherAssert.assertThat(
        output,
        new org.hamcrest.core.SubstringMatcher(
            String.format("latest: digest: %s", original.digest())
        ) {
            @Override
            protected boolean evalSubstringOf(String s) {
                return s.contains(this.substring);
            }

            @Override
            protected String relationship() {
                return "containing";
            }
        }
    );
}
```