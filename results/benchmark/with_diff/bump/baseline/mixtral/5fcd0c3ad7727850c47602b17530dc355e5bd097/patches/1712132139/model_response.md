Based on the error message and the library changes, it seems that the `getClassInfo` method of `CoverageDatabase` is no longer available in the new library version. Instead, there is a new `getClassInfo` method in `ClassInfoBuilder` that takes `ClassName`, `byte[]`, and `long` as parameters.

To fix the error, you can modify the `createSummaryData` method to first create a `ClassInfoBuilder` object using the mutated class name, and then use the new `getClassInfo` method to get the `ClassInfo` object. Here's the proposed patch:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfoBuilder builder = ClassInfo.builder(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(builder.getClassInfo()));
}
```

In this patch, we first create a `ClassInfoBuilder` object using the mutated class name. Then, we use the `getClassInfo` method of `ClassInfoBuilder` to get the `ClassInfo` object, which can be passed to the `getClassInfo` method of `CoverageDatabase`. This should fix the error caused by the missing `getClassInfo` method of `CoverageDatabase`.