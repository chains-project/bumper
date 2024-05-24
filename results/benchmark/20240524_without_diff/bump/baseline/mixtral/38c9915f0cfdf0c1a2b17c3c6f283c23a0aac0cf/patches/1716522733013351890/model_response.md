Here's the proposed patch:
```java
import org.cactoos.iterable.Filtered;

// ...

Filtered<Spendee> filteredSpendees = Filtered.with(new Func<Spendee>() {
    @Override
    public boolean check(Spendee spendee) throws Exception {
        return spendee.amount().value() > 100;
    }
}, spendees);
```
In this patch, I changed the import statement to use `org.cactoos.iterable.Filtered` instead of `org.cactoos.collection.Filtered`. The `Filtered` class has been moved from `org.cactoos.collection` to `org.cactoos.iterable` in the updated library version. The rest of the code remains unchanged.