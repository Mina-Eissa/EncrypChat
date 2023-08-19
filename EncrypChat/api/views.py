from .view.MessageListView import MessageListView
from .view.MessageCreateView import MessageCreateView
from .view.MemberCreateView import MemberCreateView
from .view.MemberReadView import MemberReadView
Message_List = MessageListView.as_view()
Message_Create = MessageCreateView.as_view()
Member_Create = MemberCreateView.as_view()
Member_Read = MemberReadView.as_view()
