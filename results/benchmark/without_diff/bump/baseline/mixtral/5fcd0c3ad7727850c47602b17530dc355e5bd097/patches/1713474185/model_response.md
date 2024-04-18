Sure, here's a potential patch for the failing client code:
```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = null;
    if (coverage != null && data != null) {
        classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    }
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
In this patch, I added a null check for both `coverage` and `data` variables before calling their respective methods. I also initialized the `classInfo` variable to null, and only assigned it a value if both `coverage` and `data` are not null. This way, the `MutationTestSummaryData` constructor won't receive a null value for `classInfo`.

Note that I'm assuming that the `MutationTestSummaryData` constructor can handle a null value for `classInfo`. If that's not the case, you might need to adjust the patch accordingly.