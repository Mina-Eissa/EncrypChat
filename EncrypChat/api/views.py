from .view.MessageListView import MessageListView
from .view.MessageCreateView import MessageCreateView
from .view.MemberCreateView import MemberCreateView
from .view.MemberDetailsView import MemberDetailsView
from .view.ChatCreateView import ChatCreateView
Message_List = MessageListView.as_view()
Message_Create = MessageCreateView.as_view()
Member_Create = MemberCreateView.as_view()
Member_Details = MemberDetailsView.as_view()
Chat_Create = ChatCreateView.as_view()

