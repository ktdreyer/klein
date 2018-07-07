from typing import TYPE_CHECKING

from ._iform import (
    ValidationError,
    ValueAbsent,
)
from ._interfaces import (
    IKleinRequest,
)
from ._isession import (
    EarlyExit,
    IDependencyInjector as _IDependencyInjector,
    IRequestLifecycle as _IRequestLifecycle,
    IRequiredParameter as _IRequiredParameter,
    ISession as _ISession,
    ISessionProcurer as _ISessionProcurer,
    ISessionStore as _ISessionStore,
    ISimpleAccount as _ISimpleAccount,
    ISimpleAccountBinding as _ISimpleAccountBinding,
    NoSuchSession,
    SessionMechanism,
    TooLateForCookies,
    TransactionEnded,
)

if TYPE_CHECKING:               # pragma: no cover
    from ._storage.memory import MemorySessionStore, MemorySession
    from ._storage.sql import (SessionStore, SQLAccount, IPTrackingProcurer,
                               AccountSessionBinding)
    from ._session import SessionProcurer, Authorization
    from ._form import Field, RenderableFormParam, FieldInjector
    from ._isession import IRequestLifecycleT as _IRequestLifecycleT

    from typing import Union

    ISessionStore = Union[_ISessionStore, MemorySessionStore,
                          SessionStore]
    ISessionProcurer = Union[_ISessionProcurer, SessionProcurer,
                             IPTrackingProcurer]
    ISession = Union[_ISession, MemorySession]
    ISimpleAccount = Union[_ISimpleAccount, SQLAccount]
    ISimpleAccountBinding = Union[_ISimpleAccountBinding,
                                  AccountSessionBinding]
    IDependencyInjector = Union[_IDependencyInjector, Authorization,
                                RenderableFormParam, FieldInjector]
    IRequiredParameter = Union[_IRequiredParameter, Authorization, Field,
                               RenderableFormParam]
    IRequestLifecycle = _IRequestLifecycleT
else:
    ISession = _ISession
    ISessionStore = _ISessionStore
    ISimpleAccount = _ISimpleAccount
    ISessionProcurer = _ISessionProcurer
    ISimpleAccountBinding = _ISimpleAccountBinding
    IDependencyInjector = _IDependencyInjector
    IRequiredParameter = _IRequiredParameter
    IRequestLifecycle = _IRequestLifecycle

__all__ = (
    "IKleinRequest",
    "NoSuchSession",
    "TooLateForCookies",
    "TransactionEnded",
    "ISessionStore",
    "ISimpleAccountBinding",
    "ISimpleAccount",
    "ISessionProcurer",
    "IDependencyInjector",
    "IRequiredParameter",
    "IRequestLifecycle",
    "EarlyExit",
    "SessionMechanism",
    "ISession",
    "ValidationError",
    "ValueAbsent",
)
