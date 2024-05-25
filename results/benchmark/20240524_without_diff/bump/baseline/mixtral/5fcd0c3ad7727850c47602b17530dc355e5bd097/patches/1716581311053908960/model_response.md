Here is a possible patch for the failing client code:

```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    String mutatedClass = data.getMutatedClass();
    ClassInfo classInfo = coverage.getClassInfoIfPresent(mutatedClass);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo != null ? classInfo : coverage.getClassInfo(mutatedClass));
  }
```

This patch checks if `getClassInfo` returns a non-null value before using it, and falls back to calling `getClassInfo` again with the mutated class name if it is null. This should avoid the `cannot find symbol` error, since `getClassInfo` is presumably the external dependency that is causing the problem.

Note that this patch assumes that `getClassInfo` never returns a non-null value when called with a valid class name. If this assumption is incorrect, then the patch may not work correctly. In that case, a different approach may be needed.