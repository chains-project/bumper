```java
/**
 * Region.Simple can select many items.
 */
@org.junit.jupiter.api.Test
void selectsManyItems() {
    final com.jcabi.simpledb.Domain domain = this.domain();
    final int ten = 10;
    try {
        for (int idx = 0; idx < ten; ++idx) {
            domain.item(java.lang.String.format("i-%d", idx)).put("hey", "");
        }
        org.hamcrest.MatcherAssert.assertThat(domain.select(new com.amazonaws.services.simpledb.model.SelectRequest().withSelectExpression(java.lang.String.format("SELECT * FROM `%s`", domain.name())).withConsistentRead(true)), org.hamcrest.Matchers.iterableWithSize(ten));
    } finally {
        domain.drop();
    }
}
```