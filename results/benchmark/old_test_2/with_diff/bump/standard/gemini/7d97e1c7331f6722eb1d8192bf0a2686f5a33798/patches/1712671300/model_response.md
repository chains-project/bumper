```java
import static com.jcabi.matchers.RegexMatchers.matchesPattern;
import static org.hamcrest.Matchers.iterableWithSize;
import static org.junit.jupiter.api.Assertions.assertThat;

import com.amazonaws.services.simpledb.model.SelectRequest;
import com.jcabi.matchers.RegexMatchers;
import com.jcabi.simpledb.Domain;
import com.jcabi.ten.Ten;
import org.hamcrest.MatcherAssert;
import org.junit.jupiter.api.Test;

/**
 * Region.Simple can select many items.
 */
@org.junit.jupiter.api.Test
void selectsManyItems() {
    final Domain domain = this.domain();
    try {
        for (int idx = 0; idx < Ten.TEN; ++idx) {
            domain.item(String.format("i-%d", idx)).put("hey", "");
        }
        MatcherAssert.assertThat(domain.select(new SelectRequest().withSelectExpression(String.format("SELECT * FROM `%s`", domain.name())).withConsistentRead(true)), iterableWithSize(Ten.TEN));
    } finally {
        domain.drop();
    }
}
```